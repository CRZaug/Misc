#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:37:38 2021

@author: camillezaug
"""


def countways(n):
   if n<0:
       return 0
   elif n == 0:
       return 1
   else:
       return countways(n-1)+countways(n-2)+countways(n-3)
   


def cwFast(n,memo):
    if n<0:
        return 0
    elif n==0:
        return 1
    elif memo[n]>-1:
        return memo[n]
    else:
        memo[n]=cwFast(n-1,memo)+cwFast(n-2,memo)+cwFast(n-3,memo)
        return memo[n]



memo = [-1]*4
# print(countways(3))
print(cwFast(3,memo))