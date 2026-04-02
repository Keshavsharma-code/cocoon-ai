from rich.console import Console

console = Console()

class SilkLogger:
    @staticmethod
    def info(msg: str):
        console.print(f"[bold blue]INFO:[/bold blue] {msg}")

    @staticmethod
    def success(msg: str):
        console.print(f"[bold green]SUCCESS:[/bold green] {msg}")

    @staticmethod
    def error(msg: str):
        console.print(f"[bold red]ERROR:[/bold red] {msg}")
