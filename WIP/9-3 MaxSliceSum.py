#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:27:39 2020

@author: reejungkim
"""

#9-3 MaxSliceSum

def solution(A):
    # write your code in Python 3.6

    arr = []

    for x in range(0, len(A)):
        for y in range(x+1, len(A)+1):
            arr.append(sum(A[x:y]))
        #print(arr)
    
    return max(arr)


    pass
