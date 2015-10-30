#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Число 125874 и результат умножения его на 2 — 251748 можно
получить друг из друга перестановкой цифр.
Найдите наименьшее положительное натуральное x такое,
что числа 3*x, 6*x можно получить друг из друга перестановкой цифр.
'''
x = 1
y = 3*x
number1 = y
number2 = 2*y

for i in range(1,100000):
    k1 = list(str(3*i))
    k2 = list(str(6*i))
    if sorted(k1) == sorted(k2):
        print(i, "Cograts!")

#41958