#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 01:16:06 2020

@author: reejungkim
"""

def solution(A):
    # write your code in Python 3.6

    A = sorted(A)
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])

    pass