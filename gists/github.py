import os

import requests

from . import exceptions


class GithubApi:
    BASE_URL = "https://api.github.com"

    def __init__(self, custom_token=None):
        token = os.getenv("GH_TOKEN", custom_token)

        if not token:
            raise exceptions.GithubApiTokenNotFound()

        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {token}",
        }

    def get(self, path, **kwargs):
        ...