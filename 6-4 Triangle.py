#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 00:24:07 2020

@author: reejungkim
"""

# 6-4 Triangle


def solution(A):
    # write your code in Python 3.6
    
    A = sorted(A)
  

    for i in range(len(A)-2):
        if A[i] + A[i+1]> A[i+2] :
            return 1
    return 0

    pass