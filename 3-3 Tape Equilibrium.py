#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 00:01:26 2020

@author: reejungkim
"""


def solution(A):
    # write your code in Python 3.6
    

    sum1 = sum(A)
    sum2 = 0
    diff = []


    for i in A[:-1]:
        sum2 += i
        diff.append(abs(sum1 - 2*sum2))

    return min(diff)


    pass