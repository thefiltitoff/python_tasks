def fast_mul(x, y, result=0):
    if (x == 0) or (y == 0):
        return 0
    elif x == 1:
        return result + y
    elif x % 2 != 0:
        result += y
    return fast_mul(x // 2, y * 2, result)


print(fast_mul(10, 15))
