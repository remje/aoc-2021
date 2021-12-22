from pathlib import Path
from re import search
from typing import TextIO


def gamma_rate(data: TextIO):
    counters: list[int] = []
    nb_lines: int = 0
    for line in data:
        nb_lines += 1
        for position, char in enumerate(line.rstrip()):
            if len(counters) < position + 1:
                counters.append(int(char))
            else:
                counters[position] += int(char)
    most_frequent_values = [round(counter / nb_lines) for counter in counters]
    return ''.join(str(value) for value in most_frequent_values)


def epsilon_rate(gamma_rate: str):
    return ''.join('0' if value == '1' else '1' for value in gamma_rate)


def part_1(input: Path):
    with open(file=input, mode='r') as f:
        gamma = gamma_rate(f)
        epsilon = epsilon_rate(gamma)
        return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    path = Path('./src/day3/input.txt')
    print(part_1(path))
