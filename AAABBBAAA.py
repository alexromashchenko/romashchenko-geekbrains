# coding: utf-8

n = int(input('Введите количество строк = n'))
m = int(input('Введите количество повторений троек ААА = m'))

a = "AAA"
b = "BBB"

for i in range(n):
    stroka1 = (a + b) * m
    stroka2 = (b + a) * m
    print(stroka1)
    print(stroka2)