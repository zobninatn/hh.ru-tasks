#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Полином
Дано выражение, содержащее скобки, операции сложения, вычитания, умножения,
возведения в константную степень и одну
переменную, например: (x - 5)(2x^3 + x(x^2 - 9)).

Представьте это выражение в развёрнутом виде, например:
3x^4 - 15x^3 - 9x^2 + 45x
pure_data = "4(x - 5)(2x^3 + x(x^2 - 9))"
variable = 'x'
def data_format(expression, variable):
#pure_data = input("Enter an expression: ")

    bpd = expression #a little Bit Parsed Data
    bpd = bpd.replace(" ", "").replace(")(", ")*(").replace(")" + variable, ")*" + variable)
    bpd = bpd.replace(variable + "(", variable + "*(")
    k = 0
    for i in expression:
        if i.isdigit() == True and expression[k-1] == variable:
            bpd = bpd.replace(variable + i, i + '*' +variable)
        if i.isdigit() == True and expression[k+1] == variable:
            bpd = bpd.replace(i + variable, i + '*' + variable)
        if i.isdigit() == True and expression[k+1] == "(":
            bpd = bpd.replace(i + "(", i + '*' + "(")
        if i.isdigit() == True and expression[k-1] == ")":
            bpd = bpd.replace(")" + i, ")" + '*' + i)
        k+=1
    print("Input exp: {}\n").format(pure_data)
    print("Parsered exp: {}\n").format(bpd)
data_format(pure_data, variable)
'''
'''
функции:
1. обработки ошибок ввода
2. преобразования к опз
3. вычисления функции в опз
4. перервод из опз в развернутый вид
http://sunjay.ca/2014/04/27/evaluating-simple-math-expressions-using-python-and-regular-expressions/
'''
pure_data = "4(x - 5)(2x^3 + x(x^2 - 9))"
priority = {'+': 0,
            '-': 0,
            '*': 1,
            '^': 2}
