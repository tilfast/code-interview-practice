if __name__ == '__main__':
    nested = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested.append([name, score])

    if not len(nested) == 1:
        global_min = min(nested, key=lambda x: x[1])[1]
        nested = [i for i in nested if i[1] != global_min]

    new_min = min(nested, key=lambda x: x[1])[1]

    [print(i[0]) for i in sorted(nested, key=lambda x: x[0]) if i[1] == new_min]

