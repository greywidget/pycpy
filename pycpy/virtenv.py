from pathlib import Path
from shutil import rmtree

import typer

from pycpy import console


def delete_virtual_environment(dir: Path = Path.cwd()):
    """Delete existing Virtual Environment"""
    env_dir = dir / ".venv"
    if not env_dir.exists():
        env_dir = dir / "venv"
        if not env_dir.exists():
            console.print("No Virtual Environment Found", style="red")
            raise typer.Exit(0)

    confirm_delete = typer.confirm(f"Delete directory {env_dir}?")
    if not confirm_delete:
        console.print("Leaving directory {env_dir} in place", style="yellow")
        return

    rmtree(env_dir)
    if env_dir.exists():
        console.print(f"{env_dir} not fully deleted!", style="red")
        raise typer.Exit(0)

    console.print(f"Virtual Environment {env_dir} deleted", style="green")
