from pytest_hoverfly import hoverfly

from gists.github import GithubApi

@hoverfly('github_get')
def test_github_get():
    github_client = GithubApi()
    response = github_client.get("gists/public")
    assert response.status_code == 200
