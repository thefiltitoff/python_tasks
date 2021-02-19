
def fast_pow(x, y, res=1):
    while y > 0:
        if y == 1:
            return res * x
        if y % 2 != 0:
            res *= x
        x *= x
        y //= 2
    return res

print(fast_pow(2,4))

