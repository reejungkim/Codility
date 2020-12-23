#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 17:26:25 2020

@author: reejungkim
"""

def solution(X, A):
    # write your code in Python 3.6
    
    dict = {}
    i = 0
  

    while i < len(A):
        dict[A[i]] = i
        if len(dict) == int(X):
            return i
        i += 1
    i = -1

    return i



    pass