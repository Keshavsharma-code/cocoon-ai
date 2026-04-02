from cocoon.src.larvae import BaseLarva

class CustomLarva(BaseLarva):
    """Placeholder for user-defined specialized agents."""
    def execute(self) -> str:
        return f"Custom execution for task: {self.task}"
