#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 17:26:27 2020

@author: reejungkim
"""

def solution(A):
    # write your code in Python 3.6

    i = min(A)   
    while i > 0 :
        if i not in A:
            solution = i 
            break
        i += 1

    return solution   


