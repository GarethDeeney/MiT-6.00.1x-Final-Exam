#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 09:42:35 2020

@author: deeney
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    list1 = list(s)
    newList = []
    for i in range(0,len(list1)):
        if list1[i].isalpha() != True:
            if list1[i].isdigit() == True:
                newList += map(int, list1[i])
            
    result = 0
    if len(newList) == 0:
        return ValueError
    else:
        for i in range(0, len(newList)):
                result += newList[i]
        return result

print(sum_digits("35467"))
print(sum_digits("a;35d4"))
print(sum_digits("abdiwobfo"))
print(sum_digits("0000000"))
print(sum_digits(""))
print(sum_digits("!!£@$£%$^%$"))
print(sum_digits("!!4@$£%3^%$"))
print(sum_digits("abcdefjklmnopqrstuvwxyz123"))