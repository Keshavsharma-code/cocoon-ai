from cocoon.src.larvae import BaseLarva

class TesterLarva(BaseLarva):
    def execute(self) -> str:
        return f"Verified quality for task: {self.task}"
