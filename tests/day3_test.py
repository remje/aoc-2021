from io import StringIO
from src.day3.day3 import (
    bits_counters,
    epsilon_rate,
    gamma_rate,
    least_common_bit,
    line_count,
    most_common_bit,
    read_oxygen_generator_rating,
    read_co2_scrubber_rating,
)

INPUT_VALUES = [
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
INPUT_STRING = "\n".join((str(value) for value in INPUT_VALUES))


def test_bits_counters():
    assert bits_counters(StringIO(INPUT_STRING)) == [7, 5, 8, 7, 5]


def test_line_count():
    assert line_count(StringIO(INPUT_STRING)) == 12


def test_gamma_rate():
    gamma = gamma_rate([1, 2, 0], 3)
    assert gamma == '010'


def test_epsilon_rate():
    assert epsilon_rate('1001101') == '0110010'


def test_most_common_bit():
    counters = [1, 2, 3]
    assert most_common_bit(counters, 4, 0) == '0'
    assert most_common_bit(counters, 4, 1) == '1'
    assert most_common_bit(counters, 4, 2) == '1'


def test_least_common_bit():
    counters = [1, 2, 3]
    assert least_common_bit(counters, 4, 0) == '1'
    assert least_common_bit(counters, 4, 1) == '0'
    assert least_common_bit(counters, 4, 2) == '0'


def test_oxygen_generator_rating():
    assert read_oxygen_generator_rating(StringIO(INPUT_STRING)) == '10111'


def test_co2_scrubber_rating():
    assert read_co2_scrubber_rating(StringIO(INPUT_STRING)) == '01010'
