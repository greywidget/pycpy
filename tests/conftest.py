from pathlib import Path
from textwrap import dedent

import pytest


@pytest.fixture()
def to_dir(tmp_path: Path):
    target_directory = tmp_path / "to_dir"
    Path.mkdir(target_directory)
    return target_directory


@pytest.fixture()
def from_dir(tmp_path: Path):
    source_directory = tmp_path / "from_dir"
    Path.mkdir(source_directory)

    gitignore = source_directory / ".gitignore"
    gitignore.write_text(
        dedent(
            """\
            dist/
            venv**
            .venv**
            .env
            """
        )
    )

    pyproject = source_directory / "pyproject.toml"
    pyproject.write_text(
        dedent(
            """\
            [build-system]
            requires = ["hatchling"]
            build-backend = "hatchling.build"

            [project]
            name = "dft"
            version = "0.0.1"
            """
        )
    )

    readme = source_directory / "README.md"
    readme.write_text(
        dedent(
            """\
            # project name
            Project Description
            """
        )
    )

    return source_directory
