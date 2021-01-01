#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:26:40 2020

@author: reejungkim
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#https://app.codility.com/demo/results/trainingATWSAF-24M/
# Complexity : O(N)

def solution(A, B):
# write your code in Python 3.6
    downward = []
    survival = 0

    for size, direction in zip(A, B):
        if direction == 1:
            downward.append(size)
        else:
            while downward and downward[-1] < size:
                downward.pop()
            if downward and downward[-1]>size:
                survival +=0
            else:
                survival +=1

    return survival + len(downward)

#survival: number of fishes successfully upwarded
#downward: numbers of fishses dwonwarded