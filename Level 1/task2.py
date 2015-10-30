#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Последовательность Фиббоначи определена реккурентным соотношением
Fn = Fn-1 + Fn-2,
где F1 = 1 и F2 = 1
Первые 12 членов последовательности будут такими:
F1=1, F2=1, F3=2, F4=3, F5=5, F6=8, F7=13, F8=21, F9=34, F10=55, F11=89, F12=144
Можно увидеть, что 12-ый член последовательности - первый, состоящий из трех цифр.
Найдите номер первого члена последовательности Фиббоначи,
такого, что число цифр в нём равно 1231.
'''

i = 2
F1 = 1
F2 = 1
Fibonacci_number = 0

while len(str(Fibonacci_number)) < 1231:
    Fibonacci_number = F1 + F2
    F1 = F2
    F2 = Fibonacci_number
    i += 1
print(i)

#5888