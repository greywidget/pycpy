# pycpy
Utility project for creating/updating python projects.
Call from alias in Powershell or zsh

- `pycpy files` Copy static files to project. Handle pre-existance.
- `pycpy rmvenv` Delete existing virtual environment

## Building
- `hatch build -c -t wheel`
- Copy wheel file to `~\python_wheels`
- Install/update `pipx` from above wheel file.

## Updating with `pipx`
`pipx upgrade` expects a package, so i
- `pipx install --force C:\Users\Craig\python_wheels\pycpy-0.0.3-py3-none-any.whl`
