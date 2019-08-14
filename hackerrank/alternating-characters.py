#!/bin/python3
def alternatingCharacters(s):
    c = [1 for idx, i in enumerate(s) if s[idx] != s[idx+1]]
    return c


if __name__ == '__main__':
    q = int(input())
    result = []

    for q_itr in range(q):
        s = input()

        result.append(alternatingCharacters(s))

    print(result)
