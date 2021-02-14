# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 00:06:33 2021
Sum Square difference problem from euler

@author: Patrick
"""
sum1 = 0 
sum2 = 0

for x in range(1,101,1):
    sum1 = x * x
    sum2 = sum1 + sum2


sum3 = 0
sum4 = 0

for x in range(1,101,1):
    sum3 = sum3 + x

sum4 = sum3 * sum3

print(sum4 - sum2)