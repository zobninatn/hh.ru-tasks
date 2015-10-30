#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Для n=5 и k=3 число различных сочетаний из n по k (Cnk) равно 10:
(1,2,3), (1,2,4), (1,2,5), (1,3,4), (1,3,5), (1,4,5), (2,3,4), (2,3,5), (2,4,5) и (3,5,4)
Для какого количества пар n и k, при условии 1<=n<126 и 1<=k<n, число сочетаний
из n по k больше 1000000?
'''
import scipy.misc

counter = 0
for n in range(1, 126):
	for k in range(1, n):
		if scipy.misc.comb(n, k) > 1000000:
			counter = counter + 1
print(counter)

#6725
