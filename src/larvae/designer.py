from cocoon.src.larvae import BaseLarva

class DesignerLarva(BaseLarva):
    def execute(self) -> str:
        return f"Designed assets for task: {self.task}"
