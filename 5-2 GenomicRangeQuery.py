#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:08:43 2020

@author: reejungkim
"""


def solution(S, P, Q):
    # write your code in Python 3.6
    solutions  = []
    for k in range(len(P)):
        arr = S[P[k]: Q[k]+1]
        if 'A' in arr:
            solutions.append(1)
        elif 'C' in arr:
            solutions.append(2)
        elif 'G' in arr:
            solutions.append(3)
        else:
            solutions.append(4)
                        
    return solutions
            

    pass

