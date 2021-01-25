#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:17:11 2021

@author: camillezaug

This code looks at a square NxN matrix and does the following things:
    - returns the trace of the matrix
    - returns the number of rows with repeated values
    - returns the number of columns with repeated values
"""


def checkVestigium(matrix):
    
    
    N = len(matrix)
    
    result = [0,0,0]
    
    columnDict ={}
    for i in range(N):
        columnDict[str(i)]=[]
    
    diag=0
    columnsToCheck = [i for i in range(N)]
    for row in matrix:
        # First compute the trace
        result[0]+=row[diag]
        diag+=1
        
        
        col = 0
        rowDict = {}
        for element in row:
            
            # Check to see if there are any repeated values in the columns
            if col in columnsToCheck:
                if columnDict[str(col)].count(element)==0:
                    columnDict[str(col)].append(element)
                elif columnDict[str(col)].count(element)==1:
                    columnDict[str(col)].append(element)
                    result[2]+=1
                    columnsToCheck.remove(col)
            
            
            # Check if there are any repeated values in the rows
            if str(element) not in rowDict:
                rowDict[str(element)]=1
            elif rowDict[str(element)]==1:
                rowDict[str(element)]+=1
                result[1]+=1
                break
        
    
                    
            col+=1
    
    return result


testMatrix1 = [[1,2,3,4],[4,1,2,3],[3,4,1,2],[2,3,4,1]]
testMatrix2 = [[2,2,2,2],[2,3,2,3],[2,2,2,3],[2,2,2,2]]
testMatrix3 = [[2,1,3],[1,3,2],[1,2,3]]


print(checkVestigium(testMatrix2))