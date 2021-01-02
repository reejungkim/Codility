#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:44:52 2021

@author: reejungkim
"""

def solution(N, M):
    # write your code in Python 3.6
    return int(N/gcd(N,M))

    pass

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)