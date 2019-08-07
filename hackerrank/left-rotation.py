#!/bin/python3
# Complete the rotLeft function below.


def rotLeft(a, d):
    for _ in range(d):
        a.append(a.pop(0))
    return a


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(" ".join([str(i) for i in result]))
