# coding: utf-8
import math
print("Дано уравнение вида ax^2 + bx + c = 0")
print("Для нахождения корней уравнения, введите значение a, b, c")
a = float(input("Введите значение a"))
b = float(input("Введите значение b"))
c = float(input("Введите значение c"))
D = b ** 2 - 4 * a * c
if D < 0:
    print("Уравнение решений не имеет (комплексные числа)")
    exit()
else:
    x1 = (-b + math.sqrt(D))/ (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
print("x1=", x1, "x2=", x2)