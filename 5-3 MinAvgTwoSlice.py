#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:10:09 2020

@author: reejungkim
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#5-3 MinTwoSlice

def solution(A):
    
    N = len(A)
    
    if N == 2: 
        result = 0
        
    minimum = sum(A[0:2])/2
    result = 0

    for i in range(3,N+1):
        
        avg = sum(A[i-2:i])/2
        if avg < minimum:
            result = i-2
            minimum = avg
        
        avg = sum(A[i-3:i])/3
        if avg < min:
            result = i-3
            minimum = avg
            
    return result


    pass