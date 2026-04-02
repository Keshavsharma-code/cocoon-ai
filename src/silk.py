import time
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree
from cocoon.src.manifest import ManifestHandler
from cocoon.src.utils.logger import SilkLogger

class SilkLayer:
    def __init__(self, root: Path):
        self.root = root
        self.handler = ManifestHandler(root / "cocoon_manifest.json")

    def run_dashboard(self, hitl_callback):
        SilkLogger.info("Starting Silk Coordination Layer...")
        
        def generate_dashboard():
            manifest = self.handler.load()
            table = Table(title="Cocoon Swarm Terminal Dashboard", highlight=True)
            table.add_column("Larva (Agent)", style="cyan")
            table.add_column("Status", style="magenta")
            table.add_column("Task Progress", style="green")
            table.add_column("Cost ($)", justify="right")

            total_cost = 0.0
            for l in manifest.larvae:
                table.add_row(l.name, l.status.upper(), f"{l.task[:30]}...", f"${l.cost:.4f}")
                total_cost += l.cost

            return Panel.fit(table, title=f"🦋 Swarm: {manifest.project_name}", subtitle=f"Total Cost: ${total_cost:.4f}")

        with Live(generate_dashboard(), refresh_per_second=2) as live:
            manifest = self.handler.load()
            for l in manifest.larvae:
                if l.larva_type == "coder":
                    live.stop()
                    if not hitl_callback(l):
                        return False
                    live.start()

                l.status = "spinning"
                self.handler.save(manifest)
                time.sleep(1.0)
                l.cost += 0.05
                l.status = "silk"
                self.handler.save(manifest)
        return True
