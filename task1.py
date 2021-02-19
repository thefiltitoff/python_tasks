def fast_mul(x, y, res=0):
    if (x == 0) or (y == 0):
        return 0
    if x == 1:
        return res + y
    if x % 2 != 0:
        res += y
    return fast_mul(x // 2, y * 2, res)


print(fast_mul(10, 15))
