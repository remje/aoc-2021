from io import StringIO
from pathlib import Path
from typing import TextIO
from decimal import (
    Decimal,
    ROUND_HALF_UP,
)
from collections.abc import Callable


def bits_counters(lines: TextIO) -> list[int]:
    counters: list[int] = []
    for line in lines:
        for position, char in enumerate(line.strip('\n').strip('/n')):
            if len(counters) < position + 1:
                counters.append(int(char))
            else:
                counters[position] += int(char)
    return counters


def line_count(lines: TextIO) -> int:
    count: int = 0
    for _ in lines:
        count += 1
    return count


def gamma_rate(counters: list[int], nb_lines: int):
    most_frequent_values = [round(counter / nb_lines) for counter in counters]
    return ''.join(str(value) for value in most_frequent_values)


def epsilon_rate(gamma_rate: str):
    return ''.join('0' if value == '1' else '1' for value in gamma_rate)


def filter_lines_using_prefix(lines: TextIO, prefix: str):
    filtered_lines = []
    for line in lines:
        if str.startswith(line.strip('\n').strip('/n'), prefix):
            filtered_lines.append(line)
    return StringIO('\n'.join(filtered_lines))


def filter_lines_using_bit(lines: TextIO, bit: str, bit_position: int):
    filtered_lines = []
    for line in lines:
        line = line.strip('\n').strip('/n')
        if line[bit_position] == bit:
            filtered_lines.append(line)
    return StringIO('\n'.join(filtered_lines))


def most_common_bit(counters: list[int], nb_lines: int, bit_position: int) -> str:
    return str(Decimal(counters[bit_position] / nb_lines).quantize(Decimal('1'), rounding=ROUND_HALF_UP))


def least_common_bit(counters: list[int], nb_lines: int, bit_position: int) -> str:
    most_common = most_common_bit(counters, nb_lines, bit_position)
    return '0' if most_common == '1' else '1'


def select_on_bit_criteria(
    lines: TextIO,
    bit_position: int,
    bit_criteria: Callable[[list[int], int, int], str]
) -> TextIO:
    data = lines.read()
    counters: list[int] = bits_counters(StringIO(data))
    nb_lines = line_count(StringIO(data))
    bit_criteria_result = bit_criteria(counters, nb_lines, bit_position)
    return filter_lines_using_bit(StringIO(data), bit_criteria_result, bit_position)


def read_rating_by_filtering(lines: TextIO, bit_criteria: Callable[[list[int], int, int], str]) -> str:
    bit_position = 0
    data = lines.read()
    nb_lines = line_count(StringIO(data))
    while nb_lines > 1:
        data = select_on_bit_criteria(StringIO(data), bit_position, bit_criteria).read()
        nb_lines = line_count(StringIO(data))
        bit_position += 1
    return data


def read_oxygen_generator_rating(lines: TextIO) -> str:
    return read_rating_by_filtering(lines, most_common_bit)


def read_co2_scrubber_rating(lines: TextIO) -> str:
    return read_rating_by_filtering(lines, least_common_bit)


def part_1(input_file: Path):
    with open(file=input_file, mode='r') as f:
        counters = bits_counters(f)
    with open(file=input_file, mode='r') as f:
        nb_lines = line_count(f)
    gamma = gamma_rate(counters, nb_lines)
    epsilon = epsilon_rate(gamma)
    return int(gamma, 2) * int(epsilon, 2)


def part_2(input_file: Path):
    with open(file=input_file, mode='r') as f:
        oxygen_generator_rating: int = int(read_oxygen_generator_rating(f), 2)
    with open(file=input_file, mode='r') as f:
        co2_scrubber_rating: int = int(read_co2_scrubber_rating(f), 2)
    life_support_rating: int = oxygen_generator_rating * co2_scrubber_rating
    return life_support_rating


if __name__ == "__main__":
    path = Path('./src/day3/input.txt')
    print(part_1(path))
    print(part_2(path))
