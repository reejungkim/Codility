#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:00:42 2020

@author: reejungkim
"""

def solution(A):
    # write your code in Python 3.6
    total = 0
    length_A = len(A)
    
    for i in range(0, length_A) :
        total += A[i] 
    true_total = (length_A+1)*(length_A+1+1)/2
    missing = true_total - total 
    
    return int(missing)


    pass
