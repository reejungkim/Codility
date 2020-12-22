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
                arr_diff.append( arr[x] - arr[x-1] )
    
    max_N = max(arr) +1
    min_N = min(arr) +1
    print(max_N)
    print(min_N)
    if max(arr_diff) >=1 :
        solution = max(arr_diff)-1
    else:
        solution = 0
        
    return solution
    
pass
