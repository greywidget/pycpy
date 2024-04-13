import typer

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
        print("Bypassing project file copy")
        typer.Exit()
