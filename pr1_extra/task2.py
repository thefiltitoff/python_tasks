
def fast_pow(x, y, result=1):
    while y > 0:
        if y == 1:
            return result * x
        if y % 2 != 0:
            result *= x
        x *= x
        y //= 2
    return result

print(fast_pow(2,4))

