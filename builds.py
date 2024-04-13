from pathlib import Path

import typer

from pycpy import STATIC_DIR


def _process_file(to_file: Path, data: str):
    if to_file.exists():
        overwrite = typer.confirm(f"{to_file.name} already exists. Overwrite it?")
        if not overwrite:
            print(f"Leaving existing file {to_file.name}")
            return

        to_file.unlink()
        print(f"Overwriting existing file {to_file.name}")

    to_file.write_text(data)


def git_ignore(to_dir: Path = Path.cwd()):
    name = ".gitignore"
    from_file = STATIC_DIR / name
    data = from_file.read_text()
    to_file = to_dir / name

    _process_file(to_file, data)
