# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:32:05 2021

@author: Patrick
"""

from math import *

def get_sum(num1: int=1, num2: int=1):
    return num1 + num2

def get_sum2(*args):
    sum = 0
    
    for arg in args:
        sum += arg
    return sum

print(get_sum2(5, 6, 7, 8, 9, 20, 25))

def next_2(num):
    return num + 1, num + 3

i1, i2 = next_2(5)
print (i1, i2)

def mult_by(*args):
    product_list = []
    for arg in args:
       product_list.append(lambda arg: arg * arg)
    return product_list




def mult_list(list, func):
    for x in list:
        print(func(x))




lam_list = [lambda x: x **2,
            lambda x: x ** 3]

new_list = mult_by(5,7,8)

    


