from typing import List, Optional
from pathlib import Path
from cocoon.src.models.swarm import TaskDecomposition, SubTask, LarvaType, LarvaInfo
from cocoon.src.manifest import ManifestHandler
from cocoon.src.utils.logger import SilkLogger

class Hatchery:
    def __init__(self, root: Path):
        self.root = root
        self.handler = ManifestHandler(root / "cocoon_manifest.json")

    def decompose_goal(self, goal: str, budget: float = 5.0, iterations: int = 10) -> TaskDecomposition:
        SilkLogger.info(f"Decomposing goal: {goal}")
        # In a real swarm, this calls the LLM with structured output Pydantic models.
        # For the professional structure, we return the Snake Game model as a baseline.
        subtasks = [
            SubTask(name="plan", description="Plan the system.", larva_type=LarvaType.PLANNER),
            SubTask(name="code", description="Write the code.", larva_type=LarvaType.CODER, dependencies=["plan"]),
            SubTask(name="review", description="Review the code.", larva_type=LarvaType.REVIEWER, dependencies=["code"])
        ]
        return TaskDecomposition(goal=goal, subtasks=subtasks, max_budget=budget, max_iterations=iterations)

    def hatch_subtask(self, subtask: SubTask) -> LarvaInfo:
        larva = LarvaInfo(
            name=subtask.name,
            larva_type=subtask.larva_type.value,
            task=subtask.description,
            status="hatching"
        )
        self.handler.add_larva(larva)
        return larva
