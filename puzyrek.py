def po_vozr(l):
    for i in range(0, (int(len(l)))):
        for j in range(int(len(l)-1) - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    return l
stroka = [3, -13, 1234, 18, 16.15, 3.18, -15000, 25, 19, 67]
print(type(stroka))
res = po_vozr(stroka)
print(res)
