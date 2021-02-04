#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:34:23 2020

@author: deeney
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here
    
    map_keys = map_from
    map_values = map_to
    key_code = dict(zip(map_keys, map_values))
    list1 = map(str, code)
    decoded = ''
    for i in list1:
        i.replace(i, map_values)
        decoded += i
    return key_code, decoded

print(cipher("abcd","dcba","dab"))
