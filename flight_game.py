from ursina import *
import random

# --- Infinite Flight 3D ---
app = Ursina()

# Window configuration
window.title = "Cocoon: Infinite Flight 3D"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

# --- Entities ---
sky = Sky()
plane = Entity(model='cube', color=color.white, scale=(1, 0.5, 2), position=(0, 0, 0), texture='white_cube')
# Add wings to make it look slightly more like a plane
wings = Entity(parent=plane, model='cube', color=color.light_gray, scale=(4, 0.1, 0.5))

# --- Game State ---
score = 0
score_text = Text(text=f'Gems Collected: {score}', position=(-0.85, 0.45), scale=2, color=color.yellow)
speed = 20

# --- Sky Objects (Gems) ---
gems = []

def spawn_gem():
    new_gem = Entity(
        model='sphere', 
        color=color.gold, 
        scale=0.5, 
        position=(random.uniform(-10, 10), random.uniform(-5, 10), 50),
        collider='sphere'
    )
    gems.append(new_gem)

# Spawn initial gems
for _ in range(10):
    spawn_gem()

# --- Main Game Loop ---
def update():
    global score, speed
    
    # Plane Movement (Input)
    if held_keys['w']: plane.y += 5 * time.dt
    if held_keys['s']: plane.y -= 5 * time.dt
    if held_keys['a']: plane.x -= 8 * time.dt
    if held_keys['d']: plane.x += 8 * time.dt
    
    # Infinite Cloud Movement (Background simulation)
    for gem in gems:
        gem.z -= speed * time.dt
        
        # Collision Detection
        if gem.intersects(plane).hit:
            score += 1
            score_text.text = f'Gems Collected: {score}'
            gem.position = (random.uniform(-10, 10), random.uniform(-5, 10), 50)
            speed += 0.5 # Gradually increase speed
            
        # Reset gems that fly past the plane
        if gem.z < -5:
            gem.position = (random.uniform(-10, 10), random.uniform(-5, 10), 50)

# Instruction Text
instructions = Text(
    text="Use W/A/S/D to Fly. Collect the Golden Gems!", 
    position=(0, -0.4), 
    origin=(0,0), 
    color=color.cyan
)

app.run()
