#!/usr/local/bin/python3


def part_1(values):
    valids = 0

    for value in values:
        space_split = value.split(" ")
        amounts = space_split[0].split("-")
        letter = space_split[1][:-1]
        password = space_split[2]

        if int(amounts[0]) <= password.count(letter) <= int(amounts[1]):
            valids += 1

    return valids

def part_2(values):
    valids = 0

    for value in values:
        space_split = value.split(" ")
        indices = space_split[0].split("-")
        letter = space_split[1][:-1]
        password = space_split[2]

        is_first_index = password[int(indices[0]) - 1] == letter
        is_second_index = password[int(indices[1]) - 1] == letter

        if (is_first_index != is_second_index):
            valids += 1

    return valids


if __name__ == "__main__":
    with open("input.txt") as f:
        values = f.readlines()

    print(f"Part 1: {part_1(values)}")
    print(f"Part 2: {part_2(values)}")







