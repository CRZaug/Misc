"""
Make it to the end of array in min number of moves. Can move 1 or 2 places at a time, but must NEVER "land" on a 1.

"""


import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    # We're assuming 1s can ONLY be surrounded by 0s
    # Otherwise one cannot win the game.

    jumps = 0
    i=0
    while i <len(c)-1:
        
        if i+2<=len(c)-1 and c[i+2]==0:
            print("two jumps")
            jumps +=1
            i +=2
            print(i)
    
        elif i+1<=len(c)-1 and c[i+1]==0:
            print("one jump")
            jumps+=1
            i+=1
            print(i)
        elif i == len(c):
            i+=1
            print("reached the end")
        else:
            print("wrong",i)
            i+=1
            
            
    return jumps 
    
    
    
    # If there is ever a two and a 1 together, that means we have a choice
    # How do we decide?
    

if __name__ == '__main__':
    
    c = [0, 1, 0, 0,0 , 0,0]

    result = jumpingOnClouds(c)

    print(result)
    