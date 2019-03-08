# coding: utf-8
import random
import pprint

n = int(input("Import matrix' size"))

matr = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(0)

    matr.append(row)

pprint.pprint(matr)

for i in range(n):
    for j in range(n):
        matr[i][j] = random.randint(1, 99)

for i in range(n):
    for j in range(n):
        j = random.randint(0, n-1)
        matr[i][j] = 0
        break
pprint.pprint(matr)