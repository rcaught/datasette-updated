# datasette-updated

[![PyPI](https://img.shields.io/pypi/v/datasette-updated.svg)](https://pypi.org/project/datasette-updated/)
[![Changelog](https://img.shields.io/github/v/release/rcaught/datasette-updated?include_prereleases&label=changelog)](https://github.com/rcaught/datasette-updated/releases)
[![Tests](https://github.com/rcaught/datasette-updated/workflows/Test/badge.svg)](https://github.com/rcaught/datasette-updated/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/rcaught/datasette-updated/blob/main/LICENSE)

Display the date your data was last updated

## Installation

Install this plugin in the same environment as Datasette.
```bash
datasette install datasette-updated
```
## Usage

```bash
DATASETTE_UPDATED=$(date -Iseconds) datasette ...
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd datasette-updated
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
pytest
```
