from pathlib import Path

import typer

from . import console
from .builds import git_ignore, pyproject, readme
from .virtenv import delete_virtual_environment

app = typer.Typer(add_completion=False)


@app.command()
def files():
    """
    Copy project scripts to new project directory\n
    - .gitignore\n
    - pyproject.toml\n
    - README.md
    """
    copy_files = typer.confirm("Copy default project files?")
    if not copy_files:
        console.print("Bypassing project file copy", style="yellow")
        raise typer.Exit(0)

    git_ignore()
    pyproject()
    readme()


@app.command()
def rmvenv(dir: Path = Path.cwd()):
    """Delete existing Virtual Environment"""
    delete_virtual_environment(dir)
