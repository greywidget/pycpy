from pathlib import Path

from rich.console import Console

PLACEHOLDER_NAME = "dft"
PROJECT_NAME = Path.cwd().name
STATIC_DIR = Path.home() / "python_static"

console = Console()
