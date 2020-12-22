#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 12:25:39 2020

@author: reejungkim
"""
def solution(A, K):
   
    if len(A)>0:
        temp_list = A
        for i in range(0, K):
            temp_list =    rotate_list(temp_list, K)
        solution = temp_list
    else:
        solution =  A
        
    return solution 
        
pass




def rotate_list(A, K):
    
    length_A = len(A)
    arr = [] 
    
    
    last = A[length_A-1]
    arr.append(last)

    for i in range(0, length_A-1):
        temp = A[i]
        arr.append(temp)
    
    return arr
pass