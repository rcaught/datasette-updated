# datasette-updated

[![PyPI](https://img.shields.io/pypi/v/datasette-updated.svg)](https://pypi.org/project/datasette-updated/)
[![Changelog](https://img.shields.io/github/v/release/rcaught/datasette-updated?include_prereleases&label=changelog)](https://github.com/rcaught/datasette-updated/releases)
[![Tests](https://github.com/rcaught/datasette-updated/workflows/Test/badge.svg)](https://github.com/rcaught/datasette-updated/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/rcaught/datasette-updated/blob/main/LICENSE)

Display the date your data was updated

## Installation

Install this plugin in the same environment as Datasette.
```bash
datasette install datasette-updated
```
## Usage

You can have a different updated per table, database or Datasette instance. If undefined at any level, values will fall back in that order.

If you have known static values, you can define them in your base `metadata.(json|yml)``:
```json
{
  "plugins": {
    "datasette-updated": {
      "updated": "2023-12-14T23:04:42+00:00"
    }
  },
  "databases": {
    "my-database-name": {
      "plugins": {
        "datasette-updated": {
          "updated": "2023-01-01T00:00:00+00:00"
        }
      },
      "tables": {
        "my-table-name": {
          "plugins": {
            "datasette-updated": {
              "updated": "2020-01-01T00:00:00+00:00"
            }
          }
          ...
```

If you want to define dynamic value(s) on `datasette package` or `datasette publish`, put metadata for this plugin in `YOUR_PLUGINS_DIR/datasette-updated/metadata.json`.
```sh
mkdir -p plugins/datasette-updated/ && \
echo <<-END
{
  "plugins": {
    "datasette-updated": {
      "updated": "$(date -Iseconds)"
    }
  }
}
END
> plugins/datasette-updated/metadata.json
&& datasette publish --plugins-dir=plugins ...
```

Combining static and dynamic configuration is possible, but be aware that the base `metadata.(json|yml)` will always win if there is a duplicate configuration value.

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
