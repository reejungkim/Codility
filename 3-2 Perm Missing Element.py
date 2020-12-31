#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:00:42 2020

@author: reejungkim
"""


def solution(A):
    # write your code in Python 3.6
    total = sum(A)
    total_expected = (len(A)+2) * (len(A)+1) //2

    return total_expected - total

    pass