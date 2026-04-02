import sys
import click
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from cocoon.src.manifest import ManifestHandler, LarvaInfo
from cocoon.src.hatchery import Hatchery
from cocoon.src.silk import SilkLayer
from cocoon.src.emerge import EmergeHarvester
from cocoon.src.bloom import BloomEngine
from cocoon.src.utils.logger import SilkLogger

console = Console()

@click.group()
@click.option("--project-root", default=".", help="Root directory of the Cocoon project")
@click.pass_context
def cli(ctx, project_root):
    ctx.obj = {"root": Path(project_root).resolve()}

@cli.command(help="Initialize cocoon (init alias for spin)")
@click.option("--name", required=True)
@click.option("--max-budget", default=5.0, help="Max USD budget for the swarm")
@click.pass_context
def spin(ctx, name, max_budget):
    """Phase: Egg - Initialize a new Cocoon project."""
    root = ctx.obj["root"]
    manifest_path = root / "cocoon_manifest.json"
    handler = ManifestHandler(manifest_path)
    
    if manifest_path.exists():
        SilkLogger.error(f"Cocoon at {root} already exists.")
    else:
        manifest = handler.load()
        manifest.project_name = name
        manifest.max_budget = max_budget
        handler.save(manifest) 
        console.print(Panel(f"🚀 [bold blue]Cocoon Spun:[/bold blue] {name}\nBudget Limit: ${max_budget}", title="Egg Phase"))

@cli.command()
@click.option("--task", required=True)
@click.option("--max-iterations", default=10, help="Max iterations for the swarm")
@click.pass_context
def hatch(ctx, task, max_iterations):
    """Phase: Larva - Decompose goal and spawn specialized larvae."""
    root = ctx.obj["root"]
    hatchery = Hatchery(root)
    SilkLogger.info(f"Hatching Larvae for task: {task}")
    
    decomposition = hatchery.decompose_goal(task, iterations=max_iterations)
    
    for subtask in decomposition.subtasks:
        info = hatchery.hatch_subtask(subtask)
        SilkLogger.success(f"Spawned {info.name} ({info.larva_type})")

    handler = hatchery.handler
    handler.update_state("larva")
    SilkLogger.success(f"Hatched {len(decomposition.subtasks)} larvae.")

@cli.command()
@click.pass_context
def silk(ctx):
    """Phase: Pupa - Run the swarm with a premium TUI dashboard."""
    root = ctx.obj["root"]
    
    def hitl_check(larva):
        console.print(f"\n✋ [bold yellow]Human-in-the-Loop Check:[/bold yellow] {larva.name} is about to weave.")
        return click.confirm("Allow this action?")

    silk_layer = SilkLayer(root)
    if silk_layer.run_dashboard(hitl_check):
        handler = ManifestHandler(root / "cocoon_manifest.json")
        handler.update_state("pupa")
        SilkLogger.success("Metamorphosis complete. Ready to 'cocoon emerge'.")
    else:
        SilkLogger.error("Swarm execution halted by user.")

@cli.command()
@click.option("--output", default="./output")
@click.pass_context
def emerge(ctx, output):
    """Phase: Imago - Harvest final flawless product."""
    root = ctx.obj["root"]
    harvester = EmergeHarvester(root)
    output_path = harvester.harvest(output)
    console.print(f"✨ [bold green]Cocoon Emerged![/bold green] Output: {output_path}")

@cli.command()
@click.option("--task", required=True)
@click.option("--generations", default=1, help="Number of generations to bloom")
@click.option("--mutation", default="optimize_hatchery", help="Mutation strategy")
@click.pass_context
def bloom(ctx, task, generations, mutation):
    """Phase: Swarm - Self-replicate and improve."""
    root = ctx.obj["root"]
    engine = BloomEngine(root)
    SilkLogger.info(f"Blooming Swarm for task: {task}")
    for gen in range(1, generations + 1):
        engine.safe_mutate(gen, mutation)

cli.add_command(spin, name="init")
cli.add_command(silk, name="run")

def main():
    cli(obj={})

if __name__ == "__main__":
    main()
