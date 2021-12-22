from io import StringIO
from pytest import raises
from src.day3.day3 import (
    epsilon_rate,
    gamma_rate,
)


def test_gamma_rate():
    input_values = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
    input_string = "\n".join((str(value) for value in input_values))
    gamma = gamma_rate(StringIO(input_string))
    assert gamma == '10110'


def test_epsilon_rate():
    assert epsilon_rate('1001101') == '0110010'


def test_invalid_data():
    input_values = ["foo", 2, 1]
    input_string = "\n".join((str(value) for value in input_values))
    with raises(ValueError):
        gamma_rate(StringIO(input_string))
