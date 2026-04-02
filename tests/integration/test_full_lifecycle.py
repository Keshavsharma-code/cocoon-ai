import unittest
from pathlib import Path
from cocoon.src.mother import cli
from click.testing import CliRunner

class TestFullLifecycle(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.temp_dir = Path("/Users/keshavsharma/.gemini/antigravity/scratch/cocoon_test")
        self.temp_dir.mkdir(parents=True, exist_ok=True)

    def test_lifecycle(self):
        # 1. Spin
        result = self.runner.invoke(cli, ["--project-root", str(self.temp_dir), "spin", "--name", "test-project"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Cocoon Spun", result.output)

        # 2. Hatch
        result = self.runner.invoke(cli, ["--project-root", str(self.temp_dir), "hatch", "--task", "Build a tool"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Hatched", result.output)

        # 3. Silk
        result = self.runner.invoke(cli, ["--project-root", str(self.temp_dir), "silk"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("weaving in parallel", result.output)

        # 4. Emerge
        result = self.runner.invoke(cli, ["--project-root", str(self.temp_dir), "emerge"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Project Emerged", result.output)

if __name__ == "__main__":
    unittest.main()
