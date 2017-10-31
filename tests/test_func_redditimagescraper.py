""" Functional test of the script. """
import os
from collections import deque

import pytest

import redditaccess
import RedditImageScraper as RSI


class MockUrl:  # pylint: disable=too-few-public-methods
    """ Mocks the url object """

    def __init__(self):
        self.created_utc = 1509231116
        self.url = "blah.jpg"


class MockSubmissions:  # pylint: disable=too-few-public-methods
    """ Mocks PRAW submission class. """

    def submissions(self, start, end):  # pylint: disable=unused-argument, no-self-use
        """ Returns a bunch of mock urls """
        urls = []
        for _ in range(1, 10):
            urls.append(MockUrl())
        return urls


class MockReddit:  # pylint: disable=too-few-public-methods
    """ Mocks PRAW reddit class. """

    def subreddit(self, name):  # pylint: disable=no-self-use
        """ returns a MockSubmissions """
        name = MockSubmissions()
        return name


class MockRequestResponse:  # pylint: disable=too-few-public-methods
    """ Mocks Requests """

    def __init__(self):
        self.content = b"blah"


def make_multiple_inputs(inputs):
    """ provides a function to call for every input requested. """

    def next_input(_):
        """ provides the first item in the list. """
        return inputs.popleft()

    return next_input


@pytest.mark.webtest
def test_functional(capfd, monkeypatch):
    """ Does a functional test of the script. """
    monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(
        deque(["2017", "10", "23", "2017", "10", "23", "wallpapers"])))
    RSI.main()
    out, _ = capfd.readouterr()

    # Check that the app states we have downloaded the file
    assert "20171023_220820_a74ga3j0lntz.png downloaded" in out
    # Check that we downloaded the expected number of images
    assert "You downloaded a total of 13 images." in out
    # Check that the file is now present
    assert os.path.isfile("20171023_220820_a74ga3j0lntz.png")


def test_functional_mock(capfd, monkeypatch):
    """ Functional test mocking praw. """

    def mockreddit():
        """ mock reddit """
        reddit = MockReddit()
        return reddit

    def mockget(_):
        """ mock get """
        results = MockRequestResponse()
        return results

    monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(
        deque(["2017", "10", "23", "2017", "10", "23", "wallpapers"])))
    monkeypatch.setattr(redditaccess, 'bot_login', mockreddit)
    monkeypatch.setattr('requests.get', mockget)
    RSI.main()
    out, _ = capfd.readouterr()

    # Check that the app states we have downloaded the file
    assert "20171028_225156_blah.jpg downloaded" in out
    # Check that we downloaded the expected number of images
    assert "You downloaded a total of 9 images." in out
    # Check that the file is now present
    assert os.path.isfile("20171028_225156_blah.jpg")
