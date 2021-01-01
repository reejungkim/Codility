#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 00:11:50 2020

@author: reejungkim
"""
def solution(A):
    # write your code in Python 3.6
    passing = 0
    east = 0
    for i, val in enumerate(A):
        if val == 0: #east
            east += 1
        else: #west
            passing += east
            if passing > 1000000000:
                return -1
    return passing
    pass
