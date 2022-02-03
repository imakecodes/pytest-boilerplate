import pytest
import requests

from dummybot import send_message

@pytest.mark.vcr()
def test_send_message():
    send_message("#dummybot", "Hello, world!")
