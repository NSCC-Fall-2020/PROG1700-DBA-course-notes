import pytest
import nbimporter

from samples import *


def test_is_palindrome():

    assert is_palindrome("mom") == True

    assert is_palindrome("racecar")

    assert not is_palindrome("palindrome")

    assert not is_palindrome("a phrase")
