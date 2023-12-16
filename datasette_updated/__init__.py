import os
from datasette import hookimpl
from datasette.utils import parse_metadata


@hookimpl
def get_metadata(datasette, key, database, table):
    try:
        datasette.plugins_dir = datasette.plugins_dir or "plugins"

        candidates = []
        for file in os.listdir(f"{datasette.plugins_dir}/datasette-updated/"):
            for extension in (".json", ".yaml", ".yml"):
                if file.endswith(extension):
                    candidates.append(
                        f"{datasette.plugins_dir}/datasette-updated/{file}"
                    )

        if len(candidates) != 0:
            updated_file = open(
                candidates[0],
                "r",
                encoding="utf8",
            )

            with updated_file:
                return parse_metadata(updated_file.read())
        else:
            raise FileNotFoundError
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
