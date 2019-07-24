def reverse(x: int) -> int:
    if len(str(abs(x))) > 9:
    #  if abs(x) >= 0xffffffff:
        return 0

    if x < 0:
        x = list(str(x))
        x = x[1:]
        x = x[::-1]
        x.insert(0, '-')
        x = ''.join(x)
    else:
        x = list(str(x))
        x = ''.join(x[::-1])

    return int(x)


print(reverse(123))
print(reverse(-123))
print(reverse(11111111111111111111111111111111111))
print(reverse(9646324351))



