#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:57:54 2021

@author: camillezaug


Return all arrays created by removing a contiguous block of length k
anywhere from the original array
"""

A = [1,2,3,4,5]
k=1


def removeKElements(Array,k):
    N = len(Array)
    result = lambda array, idx :  array[0:idx]+array[idx+k:N]
    
    return [result(A,i) for i in range(N-k+1)]


print(removeKElements(A,k))