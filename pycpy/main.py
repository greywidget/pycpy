import typer

from builds import git_ignore, pyproject, readme

from . import console

app = typer.Typer(add_completion=False)


@app.command()
def run():
    """
    PyCpy - copy project scripts to new project directory\n
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
