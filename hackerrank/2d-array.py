#!/bin/python3
# Complete the hourglassSum function below.
import logging

def hourglassSum(arr):
    rowsum = 0
    total = []

    for i in range(len(arr)):
        for j in range(len(arr)):
            rowsum = 0
            try:
                lower = arr[i+2][j-1:j+2]
                if len(lower) == 3:
                    rowsum += sum(lower)
            except:
                continue
            upper = arr[i][j-1:j+2]
            if len(upper) == 3 and len(lower) == 3:
                rowsum += sum(upper)
            try:
                if len(upper) == 3 and len(lower) == 3:
                    mid = arr[i+1][j]
                    rowsum += mid
            except:
                continue
            if len(upper) == 3 and len(lower) == 3:
                total.append(rowsum)

    return max(total)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
