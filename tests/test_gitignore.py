from unittest.mock import patch

from builds import git_ignore
from pycpy import STATIC_DIR

NAME = ".gitignore"
RANDOM_DATA = "I just make this stuff up"
FROM_FILE = STATIC_DIR / NAME


def test_new_file(tmp_path):
    data = FROM_FILE.read_text()
    to_file = tmp_path / NAME

    git_ignore(to_dir=tmp_path)

    assert to_file.exists()
    assert to_file.read_text() == data


@patch("typer.confirm")
def test_existing_file_keep(mock_typer, tmp_path):
    mock_typer.return_value = False

    to_file = tmp_path / NAME
    to_file.write_text(RANDOM_DATA)

    git_ignore(to_dir=tmp_path)
    assert to_file.read_text() == RANDOM_DATA


@patch("typer.confirm")
def test_existing_file_replace(mock_typer, tmp_path):
    mock_typer.return_value = True

    data = FROM_FILE.read_text()

    to_file = tmp_path / NAME
    to_file.write_text(RANDOM_DATA)

    git_ignore(to_dir=tmp_path)
    assert to_file.read_text() == data
