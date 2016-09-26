#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Если мы возьмем 47, перевернем его и сложим, получится число 121 — палиндром.
Если взять 349 и проделать над ним эту операцию три раза, то тоже получится палиндром:
349 + 943 = 1292
1292 + 2921 = 4213
4213 + 3124 = 7337
Найдите количество положительных натуральных чисел меньших 13850 таких,
что из них нельзя получить палиндром за 50 или менее применений описанной операции.
'''
palindrome_counter = 0
print("Computing...")
def is_palindrome(n):
    return str(n) == str(n)[::-1]

for main_number in range(13850):
    i = 0
    local_number = main_number
    for i in range(50):
        if is_palindrome(local_number):
            palindrome_counter += 1
            break
        else:
            local_number += int(str(local_number)[::-1])
        i += 1
print("Hooray!")
print(palindrome_counter)
print(13850 - palindrome_counter)
#388 или 392
