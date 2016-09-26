#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Запись n! обозначает число равное произведению n*(n-1)*(n-2)*...*1 и называется факториал.
Например, 6! = 6*5*4*3*2*1 = 720.
Сумма всех цифр в факториале 6 равна 7+2+0=9
Найдите сумму всех цифр в 303!
'''

n = 303
factorial = 1
number = 0
sum_of_ints = 0
while number < n:
    number += 1
    factorial = factorial * number

for i in str(factorial):
     sum_of_ints += int(i)
print(sum_of_ints)

#вроде 2493
