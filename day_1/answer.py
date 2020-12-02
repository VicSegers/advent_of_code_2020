#!/usr/local/bin/python3

def part_1(values, target):
    for value in values:
        for value2 in values:
            if value + value2 == 2020:
                return value * value2

def part_2(values, target):
    for value in values:
        for value2 in values:
            for value3 in values:
                if value + value2 + value3 == 2020:
                    return value * value2 * value3


if __name__ == "__main__":
    with open("input.txt") as f:
        values = [int(line[:-1]) for line in f.readlines()]

    print(f"Part 1: {part_1(values, 2020)}")
    print(f"Part 2: {part_2(values, 2020)}")
