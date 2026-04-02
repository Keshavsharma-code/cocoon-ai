from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from enum import Enum
from dataclasses import dataclass

class LarvaType(str, Enum):
    PLANNER = "planner"
    CODER = "coder"
    REVIEWER = "reviewer"
    SCRAPER = "scraper"
    DESIGNER = "designer"
    TESTER = "tester"

class SubTask(BaseModel):
    name: str = Field(..., description="Unique name for the subtask")
    description: str = Field(..., description="Detailed instructions for the larva")
    larva_type: LarvaType = Field(..., description="The specialized larva required for this task")
    dependencies: List[str] = Field(default_factory=list, description="Names of previous subtasks required")

class TaskDecomposition(BaseModel):
    goal: str
    subtasks: List[SubTask]
    max_budget: float = 5.0
    max_iterations: int = 10

class LarvaStatus(str, Enum):
    EGG = "egg"
    HATCHING = "hatching"
    SPINNING = "spinning" # Active work
    SILK = "silk"         # Completion pending review
    EMERGED = "emerged"   # Fully complete
    FAILED = "failed"

@dataclass
class LarvaInfo:
    name: str
    larva_type: str
    task: str
    status: str = "egg"
    cost: float = 0.0
    iterations: int = 0
    pid: Optional[int] = None
    output_dir: Optional[str] = None

class CocoonManifest(BaseModel):
    project_name: str
    version: str = "0.1.0"
    larvae: List[Dict] = Field(default_factory=list)
    state: str = "egg"
    max_budget: float = 5.0
    last_metamorphosis: Optional[float] = None
