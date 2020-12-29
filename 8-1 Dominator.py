#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 00:01:52 2020

@author: reejungkim
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")



def solution(A):
    # write your code in Python 3.6
    n = len(A)
    if n == 0:
        leader_index = -1
    elif n == 1:
        leader_index = 0
    else:
        A_sorted = sorted(A)
        candidate = A_sorted[n//2]
        count = 0
        for i in range(n):
            if A_sorted[i]==candidate  :
                count +=1
        if count > n//2 :
            leader_index = A.index(candidate)
        else:
            leader_index = -1
 
    return leader_index

    pass

