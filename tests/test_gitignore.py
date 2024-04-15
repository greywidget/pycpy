from pathlib import Path
from unittest.mock import patch

from pycpy.builds import git_ignore

NAME = ".gitignore"
RANDOM_DATA = "I just make this stuff up"


def test_git_new_file(from_dir: Path, to_dir: Path):
    from_file = from_dir / NAME
    data = from_file.read_text()
    to_file = to_dir / NAME

    git_ignore(from_dir=from_dir, to_dir=to_dir)

    assert to_file.exists()
    assert to_file.read_text() == data


@patch("typer.confirm")
def test_git_existing_file_keep(mock_typer, from_dir: Path, to_dir: Path):
    mock_typer.return_value = False

    to_file = to_dir / NAME
    to_file.write_text(RANDOM_DATA)

    git_ignore(from_dir=from_dir, to_dir=to_dir)
    assert to_file.read_text() == RANDOM_DATA


@patch("typer.confirm")
def test_git_existing_file_replace(mock_typer, from_dir: Path, to_dir: Path):
    mock_typer.return_value = True

    from_file = from_dir / NAME
    data = from_file.read_text()

    to_file = to_dir / NAME
    to_file.write_text(RANDOM_DATA)

    git_ignore(from_dir=from_dir, to_dir=to_dir)
    assert to_file.read_text() == data
