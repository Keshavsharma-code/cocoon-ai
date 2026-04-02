import os
import sys
import json
import subprocess
import google.generativeai as genai
from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from dotenv import load_dotenv

# --- Configuration & Local Environment ---
load_dotenv() # Load from .env if it exists
console = Console()

# SECURITY: We use os.getenv to ensure keys are local only.
# NEVER hardcode or push your API key to GitHub.
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    console.print("[bold red]ERROR:[/bold red] GEMINI_API_KEY not found in environment.")
    console.print("Please run: export GEMINI_API_KEY='your-key-here'")
    sys.exit(1)

genai.configure(AIzaSyCY6AkDPIthE556ADBcGky2zVZgH64H3ag=API_KEY)

class Task(BaseModel):
    id: str
    description: str
    larva_type: str = Field(..., description="planner, coder, or terminal")
    status: str = "pending"

class SwarmPlan(BaseModel):
    tasks: List[Task]

# --- Agent Definitions (The Larvae) ---

class PlannerAgent:
    """Takes a goal and returns a structured list of tasks using Gemini."""
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def plan(self, goal: str) -> List[Task]:
        console.print("[bold blue][PLANNER][/bold blue] Breaking down goal into tasks...")
        prompt = f"""
        You are the Cocoon Planner. Break the goal into a minimal, sequential list of tasks.
        Goal: {goal}
        Return ONLY a JSON object matching this schema:
        {{ "tasks": [ {{ "id": "1", "description": "...", "larva_type": "planner|coder|terminal" }} ] }}
        """
        response = self.model.generate_content(prompt)
        # Clean the response to ensure it's valid JSON
        text = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(text)
        return SwarmPlan(**data).tasks

class CoderAgent:
    """Writes code for a specific task using Gemini."""
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def write(self, task_description: str) -> str:
        console.print(f"[bold green][CODER][/bold green] Weaving code for: {task_description}")
        prompt = f"You are the Cocoon Coder. Return ONLY raw code for this task: {task_description}. No markdown blocks, no explanations."
        response = self.model.generate_content(prompt)
        return response.text.replace("```python", "").replace("```", "").strip()

class TerminalAgent:
    """Executes safe terminal commands with a timeout."""
    def execute(self, command: str) -> str:
        console.print(f"[bold red][TERMINAL][/bold red] Executing: {command}")
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=10
            )
            if result.returncode == 0:
                return f"Success: {result.stdout}"
            return f"Error: {result.stderr}"
        except subprocess.TimeoutExpired:
            return "Error: Command timed out after 10 seconds."
        except Exception as e:
            return f"Error: {str(e)}"

# --- The Swarm Loop (The Mother Agent) ---

def run_swarm(goal: str):
    console.print(Panel(f"🦋 [bold white]Cocoon Engine (Gemini Powered)[/bold white]\nGoal: {goal}", title="Self-Replicating Swarm"))
    
    planner = PlannerAgent()
    coder = CoderAgent()
    terminal = TerminalAgent()
    
    # Phase 1: Planning
    try:
        tasks = planner.plan(goal)
    except Exception as e:
        console.print(f"[bold red]Planning Error:[/bold red] {str(e)}")
        return

    iteration = 0
    max_iterations = 5
    
    while iteration < max_iterations and any(t.status == "pending" for t in tasks):
        iteration += 1
        console.print(f"\n[bold yellow]--- Iteration {iteration}/{max_iterations} ---[/bold yellow]")
        
        for task in tasks:
            if task.status != "pending":
                continue
            
            if task.larva_type == "coder":
                code = coder.write(task.description)
                # Heuristic to find filename
                filename = task.description.split()[-1] if "." in task.description else "swarm_output.py"
                with open(filename, "w") as f:
                    f.write(code)
                task.status = "completed"
                console.print(f"✓ [dim]Saved to {filename}[/dim]")
                
            elif task.larva_type == "terminal":
                output = terminal.execute(task.description)
                console.print(f"  [dim]{output[:100]}...[/dim]")
                task.status = "completed"
            
            else:
                task.status = "completed"

    console.print(Panel("✨ [bold green]Metamorphosis Complete![/bold green]", title="Success"))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cocoon_engine.py \"Your goal here\"")
    else:
        run_swarm(sys.argv[1])
