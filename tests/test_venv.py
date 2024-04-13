from pathlib import Path
from unittest.mock import patch

import click
import pytest

from pycpy.virtenv import delete_virtual_environment

RANDOM_DATA = "I just make this stuff up"


def test_no_env_found(capsys, tmp_path):
    warn_text = "No Virtual Environment Found"
    with pytest.raises(click.exceptions.Exit):
        delete_virtual_environment(tmp_path)

    output = capsys.readouterr().out.rstrip()
    assert output == warn_text


@patch("typer.confirm")
@pytest.mark.parametrize("directory_name", ["venv", ".venv"])
def test_venv_keep(mock_typer, tmp_path, directory_name):
    mock_typer.return_value = False

    # Create venv dir and file inside
    dir = tmp_path / directory_name
    Path.mkdir(dir)

    env_file = dir / "dummy.txt"
    env_file.write_text(RANDOM_DATA)
    assert env_file.exists()

    delete_virtual_environment(tmp_path)
    assert env_file.exists()


@patch("typer.confirm")
@pytest.mark.parametrize("directory_name", ["venv", ".venv"])
def test_venv_delete(mock_typer, tmp_path, directory_name):
    mock_typer.return_value = True

    # Create venv dir and file inside
    dir = tmp_path / directory_name
    Path.mkdir(dir)

    env_file = dir / "dummy.txt"
    env_file.write_text(RANDOM_DATA)
    assert env_file.exists()

    delete_virtual_environment(tmp_path)
    assert not env_file.exists()
