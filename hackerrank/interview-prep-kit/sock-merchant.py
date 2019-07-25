#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks = {}
    for i in ar:
        socks[i] = socks.get(i, 0) + 1

    pairs = [i // 2 for i in socks.values()]
    return sum(pairs)


if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
