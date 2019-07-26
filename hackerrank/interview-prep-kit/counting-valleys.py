#!/bin/python3
# Complete the countingValleys function below.


def countingValleys(n, s):
    curr_level = 0
    valleys = 0
    for i in s:
        if i == 'U':
            if curr_level < 0 and curr_level + 1 == 0:
                valleys = valleys + 1
            curr_level = curr_level + 1
        else:
            curr_level = curr_level - 1
    print(valleys)


if __name__ == '__main__':
    n = int(input())

    s = input()

    result = countingValleys(n, s)
