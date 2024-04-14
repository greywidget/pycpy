from pathlib import Path

import typer

from pycpy import PLACEHOLDER_NAME, PROJECT_NAME, STATIC_DIR, console


def _process_file(to_file: Path, data: str):
    if to_file.exists():
        overwrite = typer.confirm(f"{to_file.name} already exists. Overwrite it?")
        if not overwrite:
            console.print(f"Leaving existing file {to_file.name}", style="yellow")
            return

        to_file.unlink()
        console.print(f"Overwriting existing file {to_file.name}", style="red")

    to_file.write_text(data)


def git_ignore(from_dir: Path = STATIC_DIR, to_dir: Path = Path.cwd()):
    name = ".gitignore"
    from_file = from_dir / name
    data = from_file.read_text()
    to_file = to_dir / name

    _process_file(to_file, data)


def readme(from_dir: Path = STATIC_DIR, to_dir: Path = Path.cwd()):
    name = "README.md"
    from_file = from_dir / name
    data = from_file.read_text()
    to_file = to_dir / name

    _process_file(to_file, data)


def pyproject(from_dir: Path = STATIC_DIR, to_dir: Path = Path.cwd()):
    name = "pyproject.toml"
    from_file = from_dir / name
    data = from_file.read_text()
    data = data.replace(PLACEHOLDER_NAME, PROJECT_NAME)
    to_file = to_dir / name

    _process_file(to_file, data)
