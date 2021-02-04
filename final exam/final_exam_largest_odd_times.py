#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:52:11 2020

@author: deeney
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    if L == []:
        return None
    else:
        maxNumber = max(L)
        count = 0
        for i in range(0, len(L)):
            if L[i] == maxNumber:
                count += 1
        if count %2 == 0:
            while maxNumber in L:
                L.remove(maxNumber)
            return largest_odd_times(L)
        else:
            return maxNumber
            
    
    
#print(largest_odd_times([2,2,4,4]))
#print(largest_odd_times([3,9,5,3,5,3]))
#print(largest_odd_times([3,2,5,6,5,7]))
#print(largest_odd_times([23,23,45,78,96,11133]))
print(largest_odd_times([3,4,4,5,5,6,6,7,7,8,8,9,9,9,9]))
print(largest_odd_times([2, 2]))
print(largest_odd_times([2, 2, 4, 4]))
print(largest_odd_times([3, 2]))
print(largest_odd_times([3, 3, 2, 0]))
print(largest_odd_times([3, 0, 5, 3, 5, 3]))
print(largest_odd_times([3, 9, 5, 3, 5, 3]))
print(largest_odd_times([6, 8, 6, 8, 6, 8, 6, 8, 6, 8]))
print(largest_odd_times([2, 4, 5, 4, 5, 4, 2, 2]))

