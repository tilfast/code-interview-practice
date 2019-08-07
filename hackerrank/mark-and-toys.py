#!/bin/python3
# Complete the maximumToys function below.


def maximumToys(prices, k):
    prices = sorted(prices)
    amount = 0
    qty = []

    for i in prices:
        amount += i
        if amount < k:
            qty.append(amount)
            continue
        else:
            break

    return len(qty)


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)
