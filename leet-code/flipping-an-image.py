def flipAndInvertImage(A: list) -> list:
    print(A)
    inverted = []
    flipped = [a[::-1] for a in A]
    for x in flipped:
        inverted.append(list(map(lambda x: 0 if x == 1 else 1, x)))

    return inverted


inp = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
flipAndInvertImage(inp)
