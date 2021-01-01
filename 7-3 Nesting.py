#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 12:23:16 2021

@author: reejungkim
"""

def solution(S):
    # write your code in Python 3.6
    stack = []
    for val in S:
        if val == '(':
            stack.append('(')
        elif stack and val == ')':
            stack.pop()
        else:
            return 0
    if len(stack) == 0:
        return 1
    return 0

    pass