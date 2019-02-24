# coding: utf-8

#Методом For
x = int(input("Введите целое положительное число"))
x = str(x)
chisel = len(x)
a = 0
max = 0
#print("Количество цифр в введенном числе: ", chisel)
# При помощи for
for i in range(chisel):
   a = int(x[i])
   if a > max:
       max = a
print("Максимальная цифра в заданном числе FOR", max)

#Методом While
b = 0
MAX = 0
i = 0
while i < chisel:
    b = int(x[i])
    i = i + 1
    if b > MAX:
        MAX = b
print("Максимальная цифра в заданном числе While", MAX)

