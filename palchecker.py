# -*- coding: utf-8 -*-
"""
Project Euler
Finds largest pallindromic product of 3 digit numbers
"""


palStore = [0]
x = 999
y = 0
product = 0

for x in range(999,900,-1):
    for z in range(900,999,+1):
        product = x * z
        test = str(product)
        if test == test[::-1]:
            palStore.append(test)
print(palStore)
        
         
        