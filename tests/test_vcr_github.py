import pytest
import requests

from gists.github import GithubApi

@pytest.mark.vcr()
def test_github_get():
    github_client = GithubApi()
    response = github_client.get("gists/public")
    assert response.status_code == 200

    assert requests.get("http://httpbin.org/get").json() == {
        "args": {},
        "headers": {
          "Accept": "*/*",
          "Accept-Encoding": "gzip, deflate",
          "Host": "httpbin.org",
          "User-Agent": "python-requests/2.25.1",
          "X-Amzn-Trace-Id": "Root=1-61fa8ebd-3f9122f8579bc5c333a6b221"
        },
        "origin": "191.37.246.122",
        "url": "http://httpbin.org/get"
      }

