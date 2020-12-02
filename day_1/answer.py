#!/usr/local/bin/python3


def factor_where_sum_is(target):
    for value in values:
        for value2 in values:
            if value + value2 == 2020:
                return value * value2


if __name__ == "__main__":
    with open("input.txt") as f:
        values = [int(line[:-1]) for line in f.readlines()]

    print(factor_where_sum_is(2020))
