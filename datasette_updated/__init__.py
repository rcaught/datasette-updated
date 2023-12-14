import json
from datasette import hookimpl


@hookimpl
def startup(datasette):
    async def inner():
        versions_json = (
            await datasette.client.get(datasette.urls.path("-/versions", format="json"))
        ).json()

        if versions_json.get("datasette", {}).get("note", {}):
            try:
                result = json.loads(versions_json["datasette"]["note"])

                datasette._plugin_datasette_updated_metadata = result
            except ValueError:
                pass

    return inner


@hookimpl
def get_metadata(datasette, key, database, table):
    return getattr(datasette, "_plugin_datasette_updated_metadata", None) or {
        "plugins": {"datasette-updated": {"updated": "unknown"}}
    }


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
