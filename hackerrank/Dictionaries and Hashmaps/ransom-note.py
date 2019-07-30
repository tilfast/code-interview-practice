#!/bin/python3
# Complete the checkMagazine function below.
from collections import Counter


def checkMagazine(magazine, note):
    dmag = Counter(magazine)
    dnote = Counter(note)

    if not (dnote - dmag):
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
