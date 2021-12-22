from io import StringIO
from pytest import raises
from src.day1.day1 import (
    nb_of_increases,
    nb_of_window_increases,
)


def test_3_increases():
    input_values = [1, 2, 3, 1, 3]
    input_string = "\n".join((str(value) for value in input_values))
    assert nb_of_increases(StringIO(input_string)) == 3


def test_0_increases():
    input_values = [3, 2, 1]
    input_string = "\n".join((str(value) for value in input_values))
    assert nb_of_increases(StringIO(input_string)) == 0


def test_invalid_data():
    input_values = ["foo", 2, 1]
    input_string = "\n".join((str(value) for value in input_values))
    with raises(ValueError):
        nb_of_increases(StringIO(input_string))


def test_3_window_increases():
    input_values = [1, 1, 1, 2, 2, 2, 1]
    input_string = "\n".join((str(value) for value in input_values))
    assert nb_of_window_increases(StringIO(input_string)) == 3


def test_0_window_increases():
    input_values = [3, 3, 3, 3, 3, 2, 1]
    input_string = "\n".join((str(value) for value in input_values))
    assert nb_of_window_increases(StringIO(input_string)) == 0


def test_window_invalid_data():
    input_values = ["foo", 2, 1]
    input_string = "\n".join((str(value) for value in input_values))
    with raises(ValueError):
        nb_of_window_increases(StringIO(input_string))
