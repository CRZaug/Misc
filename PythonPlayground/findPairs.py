#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:38:58 2021

@author: camillezaug
"""


def findPairs(array,target):
    
    for i, item in enumerate(array):

        complement = target - item
        
        if complement in array[i+1:]:
            return True
        
    return False


array = [1,2,4,9]

target = 8

print(findPairs(array,target))
    
