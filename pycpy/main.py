from importlib.metadata import version
from typing import Optional

import typer
from typing_extensions import Annotated

from . import console
from .builds import git_ignore, pyproject, readme
from .virtenv import delete_virtual_environment

app = typer.Typer(add_completion=False)


@app.command()
def files():
    """
    Copy project scripts to current directory.\n
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
def rmvenv():
    """Delete existing Virtual Environment in current directory."""
    delete_virtual_environment()


def version_callback(value: bool):
    if value:
        print(f"PyCpy {version('pycpy')}")
        raise typer.Exit()


@app.callback()
def get_version(
    vers: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-V",
            callback=version_callback,
            is_eager=True,
            help="Print the version and exit.",
        ),
    ] = None,
):
    pass


if __name__ == "__main__":
    app()
