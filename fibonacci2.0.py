# coding: utf-8
def fibon(n, m):
    a = 1
    b = 1
    c = list()
    d = list()
    c.append(1)
    c.append(1)
    for i in range(0, m + 1):
        a, b = b, a + b
        c.append(b)
        if i >= (n-3) and i <= (m-3):
            d.append(b)
    return d
res = fibon(9,13)
print(res)
