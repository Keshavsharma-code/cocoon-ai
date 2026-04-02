from cocoon.src.larvae import BaseLarva

class CoderLarva(BaseLarva):
    def execute(self) -> str:
        return f"Generated code for task: {self.task}"
