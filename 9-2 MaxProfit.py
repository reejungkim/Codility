#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:54:47 2020

@author: reejungkim
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")



def solution(A):
    # write your code in Python 3.6
    max_slice = max_ending = 0
    for i in range(1, len(A)):
        max_ending = max(0, max_ending + A[i] - A[i-1])
        max_slice = max(max_slice, max_ending)
    return max_slice
    pass