#!/usr/local/bin/python3


def part_1(values):
    trees = 0
    position = 0

    for line in values:
        if line[position] == "#":
            trees += 1
        position += 3
        position %= len(line)

    return trees


def part_2(values):
    trees_1 = trees_3 = trees_5 = trees_7 = trees_2 = 0
    position_1 = position_3 = position_5 = position_7 = position_2 = 0

    for line in values:
        if line[position_1] == "#":
            trees_1 += 1
        if line[position_3] == "#":
            trees_3 += 1
        if line[position_5] == "#":
            trees_5 += 1
        if line[position_7] == "#":
            trees_7 += 1

        position_1 += 1
        position_1 %= len(line)
        position_3 += 3
        position_3 %= len(line)
        position_5 += 5
        position_5 %= len(line)
        position_7 += 7
        position_7 %= len(line)

    for line in values[::2]:
        if line[position_2] == "#":
            trees_2 += 1
        position_2 += 1
        position_2 %= len(line)

    return trees_1 * trees_2 * trees_3 * trees_5 * trees_7


if __name__ == "__main__":
    with open("input.txt") as f:
        values = [line.strip() for line in f.readlines()]

    print(f"Part 1: {part_1(values)}")
    print(f"Part 2: {part_2(values)}")
