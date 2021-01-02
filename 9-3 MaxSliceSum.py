#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 11:01:07 2021

@author: reejungkim
"""

def solution(A):
    max_ending = max_slice = A[0]
    for i in range(1, len(A)):
        max_ending = max(max_ending + A[i], A[i])
        max_slice = max(max_slice, max_ending)

    return max_slice
    pass