#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:25:43 2020

@author: reejungkim
"""

def solution(N):
    # write your code in Python 3.6
    count = 0
    import math
    rng_end = math.ceil(math.sqrt(N+1))
    for i in range(1, rng_end):
        if N % i == 0 : 
            if N/i == i:
                count +=1
            else:
                count += 2
        else:
            count += 0

    return count

    pass