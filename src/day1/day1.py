from pathlib import Path
from typing import TextIO
MAX_INT_VALUE = 232


def part_1(input: Path):
    with open(file=input, mode='r') as f:
        return nb_of_increases(f)

def part_2(input: Path):
    with open(file=input, mode='r') as f:
        return nb_of_window_increases(f)

def nb_of_increases(data: TextIO):
    nb_of_increases: int = 0
    previous_value: int = MAX_INT_VALUE
    for line in data:
        if int(line) > previous_value:
            nb_of_increases += 1
        previous_value = int(line)
    return nb_of_increases


def nb_of_window_increases(data: TextIO):
    nb_of_increases: int = 0
    previous_value: float = float('inf')
    window = []
    for line in data:
        window.append(int(line))
        if len(window) == 3:
            window_avg: float = sum(window) / len(window)
            if window_avg > previous_value:
                nb_of_increases += 1
            previous_value = window_avg
            window.pop(0)
    return nb_of_increases


if __name__ == "__main__":
    path = Path('./src/day1/input.txt')
    print(part_1(path))
    print(part_2(path))

