#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 12:16:56 2021

@author: reejungkim
"""

def solution(S):
    dict = {"{": "}", "(": ")", "[": "]"}
    stack = []

    for val in S:
        if val in "{[(":
            stack.append(val)
        elif stack and val == dict[stack[-1]]:
            stack.pop()
        else:
            return 0
    if len(stack) == 0:
        return 1
    return 0