#!/bin/python3
"""
Given two strings, we want to see if there is a common substring.
We don't care much for detail here. The substring can be anything.
It can even be a single character. In fact, that's really what we
are going to check. If there's a common substring, they definitely 
share all the same characters. 

So what we will do is create a dictionary. The keys of the dictionary will be the
characters in the string (again, we don't care what the common substrings
are, we only want to determine Tue or False). The entries in the dictionary will
be just be 1. 

After we fill in this dictionary, loop through the other string and see if
any of its chars are keys in the first one. If so, voila, we have a common substring
at the most basic level, which is what we want. If not even one character is shared,
there are definitely no larger substrings either.
"""
import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):

    # Make the dict for the longer string first
    
    lS = s1 if len(s1)>len(s2) else s2
    sS = s2 if len(s1)>len(s2) else s1
    
    comparisonDict = {}
    for char in lS:
        # If the character isn't a key, add it
        if char not in comparisonDict:
            comparisonDict[char] = 1
    
    # Now we know all the characters in the longer string. So check
    # if the shorter string has any of those chars.
    
    for char in sS:
        # If the character in the new string is already in the dict, we have 
        # a mutual substring, so return True
        if char in comparisonDict:
            return "YES"
    
    # If we make it through the whole function without finding a True, return False
    return "NO"


if __name__ == '__main__':
    
    s1 = "hello"
    s2 = "o"

    result = twoStrings(s1, s2)
    print(result)

        
