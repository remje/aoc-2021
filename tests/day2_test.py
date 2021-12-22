from io import StringIO
from pytest import raises
from src.day2.day2 import (
    final_position_and_depth,
)


def test_final_position_and_depth():
    input_values = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2"
    ]
    input_string = "\n".join((str(value) for value in input_values))
    position, depth = final_position_and_depth(StringIO(input_string))
    assert position == 15
    assert depth == 60


def test_invalid_data():
    input_values = ["foo", 2, 1]
    input_string = "\n".join((str(value) for value in input_values))
    with raises(ValueError):
        final_position_and_depth(StringIO(input_string))
