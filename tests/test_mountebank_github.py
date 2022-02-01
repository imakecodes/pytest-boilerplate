import requests
from hamcrest import assert_that
from brunns.matchers.response import is_response
from mbtest.matchers import had_request
from mbtest.imposters import Imposter, Predicate, Response, Stub
from mbtest.server import MountebankServer

from gists.github import GithubApi

import pytest
from mbtest import server

@pytest.fixture(scope="session")
def mock_server(request):
    server = MountebankServer(host="localhost", port=2525)
    return server


def test_github_get(mock_server):
    imposter = Imposter(Stub(Predicate(path="/test"),
                             Response(body="sausages")))

    with mock_server(imposter):
        # Make request to mock server - exercise code under test here
        github_client = GithubApi()
        response = github_client.get("gists/public")
        assert_that("We got the expected response",
                    response, is_response().with_status_code(200))
        response = requests.get(f"{imposter.url}/test")

        assert_that("We got the expected response",
                    response, is_response().with_status_code(200).and_body("sausages"))
        assert_that("The mock server recorded the request",
                    imposter, had_request().with_path("/test").and_method("GET"))
