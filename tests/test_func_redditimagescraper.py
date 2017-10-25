""" Functional test of the script. """
import os
from collections import deque

import RedditImageScraper as RSI


def make_multiple_inputs(inputs):
    """ provides a function to call for every input requested. """
    def next_input(_):
        """ provides the first item in the list. """
        return inputs.popleft()
    return next_input


def test_functional(capfd, monkeypatch):
    """ Does a functional test of the script. """
    monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(
        deque(["2017", "10", "23", "2017", "10", "23", "python"])))
    RSI.main()
    out, _ = capfd.readouterr()

    # Check that the app states we have downloaded the file
    assert "20171022_202306_c8y9b4m8phtz.png downloaded" in out
    # Check that we downloaded the expected number of images
    assert "You downloaded a total of 1 images." in out
    # Check that the file is now present
    assert os.path.isfile("20171022_202306_c8y9b4m8phtz.png")
