import json
from datasette import hookimpl


@hookimpl
def get_metadata(datasette, key, database, table):
    try:
        updated_file = open(
            f"{datasette.plugins_dir}/datasette-updated/metadata.json",
            "r",
            encoding="utf8",
        )

        with updated_file:
            return json.loads(updated_file.read())
    except FileNotFoundError:
        return {"plugins": {"datasette-updated": {"updated": "unknown"}}}


@hookimpl
def extra_template_vars(datasette, database, table):
    return {
        "updated": datasette.plugin_config(
            "datasette-updated", database=database, table=table
        )["updated"]
    }


@hookimpl
def extra_js_urls():
    return [
        {
            "url": "https://cdn.jsdelivr.net/npm/local-time@2.1.0/app/assets/javascripts/local-time.min.js",
            "sri": "sha384-vjSE5N9a5zc42mPRxkfhAoktbmiiZ6AIEk0mEJxR3w9SWxQdzLTQx8Y+FubMepSl",
        }
    ]


@hookimpl
def extra_body_script():
    return {
        "script": "LocalTime.start()",
    }
