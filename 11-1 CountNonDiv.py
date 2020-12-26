#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:27:09 2020

@author: reejungkim
"""

def solution(A):
    arr = []
    arr_length = []
    
    for val in A:
        arr = [i for i in A if val%i!= 0]
        #print(B)
        arr_length.append(len(arr))

    return arr_length

    pass