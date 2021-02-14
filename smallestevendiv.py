# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 23:24:57 2021
Brute Force solve for smallest number divisible by n, where n is range 1 - 20

@author: Patrick
"""

small1 = 2520
cond = False
count = 0
while(cond == False):
     for x in range (1, 21, 1):
         #print(f"X is : {x} ")
         if (small1 % x == 0):
             #print(f"The count is: {count}")
             count = count + 1
         if (count == 20):
             print(f"{small1} is the winner")
             cond = True
     print(small1)
     count = 0
     small1 = small1 + 1
    