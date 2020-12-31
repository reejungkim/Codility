#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 22:52:46 2020

@author: reejungkim
"""

def solution(A):
    # write your code in Python 3.6
    A = sorted(A)

    for i in range(0, len(A)):
        if A[i] != i+1 :
            answer = 0 #not permutation
            break
        else:
            answer = 1 #permutation
    return answer
    pass