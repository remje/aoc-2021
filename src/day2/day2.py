from pathlib import Path
from re import search
from typing import TextIO


def final_position_and_depth(data: TextIO):
    position: int = 0
    depth: int = 0
    aim: int = 0
    for line in data:
        forward = search('^forward ([0-9]+)$', line)
        down = search('^down ([0-9]+)$', line)
        up = search('^up ([0-9]+)$', line)
        if forward:
            position += int(forward.group(1))
            depth += aim * int(forward.group(1))
        elif down:
            aim += int(down.group(1))
        elif up:
            aim -= int(up.group(1))
        else:
            raise ValueError(f'Unexpected direction {line}')
    return position, depth


def part_2(input: Path):
    with open(file=input, mode='r') as f:
        position, depth = final_position_and_depth(f)
        return position * depth


if __name__ == "__main__":
    path = Path('./src/day2/input.txt')
    print(part_2(path))
