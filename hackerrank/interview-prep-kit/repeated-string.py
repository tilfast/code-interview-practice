#!/bin/python3
# Complete the repeatedString function below.


def repeatedString(s, n):
    a_count = s.count('a')

    return (a_count * (n // len(s)) + s[:n % len(s)].count('a'))


if __name__ == '__main__':
    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)
