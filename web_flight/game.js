import * as THREE from 'three';

// --- Scene Setup ---
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x87ceeb); // Sky blue
scene.fog = new THREE.Fog(0x87ceeb, 10, 100);

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById('game-container').appendChild(renderer.domElement);

// --- Lights ---
const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
directionalLight.position.set(5, 10, 7.5);
scene.add(directionalLight);

// --- Plane Entity ---
const planeGroup = new THREE.Group();

// Fuselage
const bodyGeom = new THREE.BoxGeometry(0.6, 0.4, 2);
const bodyMat = new THREE.MeshPhongMaterial({ color: 0xffffff });
const body = new THREE.Mesh(bodyGeom, bodyMat);
planeGroup.add(body);

// Wings
const wingGeom = new THREE.BoxGeometry(3, 0.05, 0.8);
const wingMat = new THREE.MeshPhongMaterial({ color: 0xcccccc });
const wings = new THREE.Mesh(wingGeom, wingMat);
wings.position.y = 0.1;
planeGroup.add(wings);

scene.add(planeGroup);
camera.position.set(0, 2, 5);
camera.lookAt(0, 0, 0);

// --- Game State ---
let score = 0;
let speed = 0.5;
const gems = [];
const scoreEl = document.getElementById('score');

// --- Input Handling ---
const keys = { w: false, a: false, s: false, d: false, ArrowUp: false, ArrowDown: false, ArrowLeft: false, ArrowRight: false };
window.addEventListener('keydown', (e) => { if (keys.hasOwnProperty(e.key)) keys[e.key] = true; });
window.addEventListener('keyup', (e) => { if (keys.hasOwnProperty(e.key)) keys[e.key] = false; });

// --- Gem Spawning ---
function spawnGem() {
    const geo = new THREE.IcosahedronGeometry(0.3, 1);
    const mat = new THREE.MeshPhongMaterial({ color: 0xffcc00, emissive: 0xaa8800 });
    const gem = new THREE.Mesh(geo, mat);
    
    gem.position.set(
        (Math.random() - 0.5) * 20,
        (Math.random() - 0.5) * 10 + 2,
        -50 - Math.random() * 50
    );
    
    scene.add(gem);
    gems.push(gem);
}

for (let i = 0; i < 15; i++) spawnGem();

// --- Game Loop ---
function animate() {
    requestAnimationFrame(animate);

    // Movement
    if (keys.w || keys.ArrowUp) planeGroup.position.y += 0.1;
    if (keys.s || keys.ArrowDown) planeGroup.position.y -= 0.1;
    if (keys.a || keys.ArrowLeft) planeGroup.position.x -= 0.1;
    if (keys.d || keys.ArrowRight) planeGroup.position.x += 0.1;

    // Boundary constraints
    planeGroup.position.x = Math.max(-8, Math.min(8, planeGroup.position.x));
    planeGroup.position.y = Math.max(-4, Math.min(6, planeGroup.position.y));

    // Gem Logic
    gems.forEach((gem, index) => {
        gem.position.z += speed;
        gem.rotation.y += 0.05;

        // Collision
        const dist = gem.position.distanceTo(planeGroup.position);
        if (dist < 1) {
            score++;
            scoreEl.innerText = `GEMS: ${score}`;
            speed += 0.005;
            resetGem(gem);
        }

        // Reset if behind
        if (gem.position.z > 10) resetGem(gem);
    });

    // Camera follow (slight)
    camera.position.x = planeGroup.position.x * 0.2;
    camera.position.y = planeGroup.position.y * 0.2 + 2;

    renderer.render(scene, camera);
}

function resetGem(gem) {
    gem.position.set(
        (Math.random() - 0.5) * 20,
        (Math.random() - 0.5) * 10 + 2,
        -50 - Math.random() * 50
    );
}

// Handle window resize
window.addEventListener('resize', () => {
    renderer.setSize(window.innerWidth, window.innerHeight);
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
});

animate();
