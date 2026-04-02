import os
import sys
from pathlib import Path
from click.testing import CliRunner
from cocoon.src.mother import cli

def run_demo():
    runner = CliRunner()
    project_root = Path("/Users/keshavsharma/.gemini/antigravity/scratch/cocoon_snake_demo")
    if project_root.exists():
        import shutil
        shutil.rmtree(project_root)
    project_root.mkdir(parents=True)

    print("--- 🦋 Cocoon 2.0: Snake Game Demo ---")
    
    # 1. Init (Spin)
    print("\n[Step 1] Initializing Swarm DNA...")
    result = runner.invoke(cli, ["--project-root", str(project_root), "init", "--name", "snake_colony", "--max-budget", "2.0"])
    print(result.output)

    # 2. Hatch
    print("\n[Step 2] Hatching specialized larvae...")
    result = runner.invoke(cli, ["--project-root", str(project_root), "hatch", "--task", "Build a terminal-based Snake game"])
    print(result.output)

    # 3. Run (Silk) - Note: In a real TUI runner, this might behave differently, but we check logic
    print("\n[Step 3] Weaving the Silk (Swarm Execution)...")
    # We mock the input for the HitL check
    result = runner.invoke(cli, ["--project-root", str(project_root), "run"], input="y\n")
    print(result.output)

    # 4. Emerge
    print("\n[Step 4] Harvesting the flawless product...")
    result = runner.invoke(cli, ["--project-root", str(project_root), "emerge"])
    print(result.output)

    snake_path = project_root / "output" / "snake.py"
    if snake_path.exists():
        print(f"✅ Success! Snake game created at: {snake_path}")
        print("Final Code Preview (first 10 lines):")
        print("\n".join(snake_path.read_text().splitlines()[:10]))
    else:
        print("❌ Failed to create snake.py")

if __name__ == "__main__":
    run_demo()
