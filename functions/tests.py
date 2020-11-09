import pytest

import nbimporter
from unit_test import *


def test_add():
    assert sum(1, 2) == 3
    assert sum(2, 2) == 4


def test_diff():
    assert diff(2, 1) == 1
    assert diff(3, 2) == 1


def test_product():
    try:
        assert product(2, 1) == 2
    except NameError:
        pytest.fail("You made an error.")