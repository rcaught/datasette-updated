import os
from datasette import hookimpl


@hookimpl
def get_metadata(datasette, key, database, table):
    return {"updated": os.getenv("DATASETTE_UPDATED", "unknown")}


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
