def f22(x):
    a = (x & 0x1ff) << 17
    b = (x & 0x3E00) << 18
    c = (x & 0x3FFFc000) >> 13
    d = (x & 0x40000000) >> 4
    e = (x & 0x80000000) >> 31
    return hex(a + b + c + d + e)


print(f22(0x25c9deb1))
print(f22(0x96b141c6))
