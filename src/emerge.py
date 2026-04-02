from pathlib import Path

class EmergeHarvester:
    def __init__(self, root: Path):
        self.root = root

    def harvest(self, output_dir: str):
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        # Harvest final results from pupated larvae
        (output_path / "final_result.txt").write_text("Metamorphosis Complete. Swarm result harvested.")
        return output_path
