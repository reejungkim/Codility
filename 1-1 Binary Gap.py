#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:31:48 2020

@author: reejungkim
"""


def solution(N):
    # write your code in Python 3.6
    print(bin(N))
    print( len(bin(N)))
    print(type( bin(N)) )

    arr = []
    for i in range(0, len(bin(N))-1): #bin(N) :
        if bin(N)[i]== '1' :
            arr.append(i)
    print(arr)

pass
