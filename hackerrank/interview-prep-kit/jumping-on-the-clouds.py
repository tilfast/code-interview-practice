#!/bin/python3
# Complete the jumpingOnClouds function below.
global steps
steps = 0


def jumpingOnClouds(c):
    try:
        global steps
        if c[2] == 0:
            jumpingOnClouds(double(c))
            steps += 1
        elif c[1] == 0:
            jumpingOnClouds(single(c))
            steps += 1
    except:
        try:
            if c[1] == 0:
                jumpingOnClouds(single(c))
                steps += 1
        except:
            pass

    return steps


def double(c):
    return c[2:]


def single(c):
    return c[1:]


if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)
