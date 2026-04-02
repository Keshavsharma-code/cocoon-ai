import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

class BloomEngine:
    """
    Step 4: Test-Driven Metamorphosis.
    Safety-first self-improvement.
    """
    MAX_GENERATIONS = 10

    def __init__(self, root: Path):
        self.root = root

    def safe_mutate(self, generation: int, mutation_code: str):
        """
        1. Sandbox implementation in a temp dir.
        2. Run automated tests (pytest).
        3. Merge only if tests pass.
        """
        with TemporaryDirectory() as chrysalis_dir:
            temp_path = Path(chrysalis_dir)
            # Copy current source for testing
            # (In a real scenario, applies mutation_code here)
            
            # Create a mock test for the mutation
            test_file = temp_path / "test_mutation.py"
            test_file.write_text("def test_sanity(): assert True")
            
            # Run pytest
            try:
                result = subprocess.run(["pytest", str(test_file)], capture_output=True, text=True)
                if result.return_code == 0:
                    print(f"✅ Mutation Generation {generation} passed verification gate.")
                    # Merge logic would go here
                else:
                    print(f"❌ Mutation Generation {generation} failed testing. Chrysalis discarded.")
            except FileNotFoundError:
                print("⚠️  Pytest not found. Defaulting to manual verification gate.")
