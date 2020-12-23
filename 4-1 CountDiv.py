#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:44:17 2020

@author: reejungkim
"""

def solution(A, B, K):
    # write your code in Python 3.6

    arr=[]
    for i in range(A, B+1):
 
        if i % K == 0:
            arr.append(i)


    return len(arr)


    pass