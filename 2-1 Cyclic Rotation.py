#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 12:25:39 2020

@author: reejungkim
"""
def solution(A, K):
    # write your code in Python 3.6
    for i in range(K):
        A = A[-1:] + A[:-1]
        
    return A
    
    pass