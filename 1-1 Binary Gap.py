#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:31:48 2020

@author: reejungkim
"""


def solution(N):
    # write your code in Python 3.6
    binary_N = bin(N)
   
    print("binary : " + binary_N)
    print("length: " + str(len(binary_N)))
    
    arr = []
    arr_diff =[]
    for i in range(2, len(binary_N)) :  
    # range starts from 2 as binary numbers always starts with "0b"
        if binary_N[i]== '1' :
            arr.append(i)
            for x in range(0, len(arr)):
                arr_diff.append( arr[x] - arr[x-1]-1 )
    
    max_N = max(arr) +1
    min_N = min(arr) +1
    print(max_N)
    print(min_N)
    if len(arr)<3:
        if max_N=="" or min_N=="" or max_N-min_N==0 :
            solution = 0
        else:
            solution = max_N - min_N -1
    else:
        solution = max(arr_diff)
        
    return solution
    
pass
