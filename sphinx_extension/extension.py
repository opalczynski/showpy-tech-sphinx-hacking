import json
import requests


def setup(app):
    requests.post(
        "https://hooks.slack.com/services/T0XXXXXXX/BXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX",
        data=json.dumps({
            "text": "Hi, there! Build made.",
            "channel": "random",
            "username": "sphinx-bot",
            "icon_emoji": ":skull:",
        })
    )
    return {'version': 'v.0.0.1'}
