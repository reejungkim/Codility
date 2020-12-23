#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 00:32:15 2020

@author: reejungkim
"""

def solution(A):
    # write your code in Python 3.6

    arr = []

    for i in A:
        if i not in arr:
            arr.append(i)
        count = len(arr)
    return count
    pass