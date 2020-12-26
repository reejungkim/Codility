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

  
    i = 0
    while i < len(B)-1: 

        if B[i] == 1 and B[i+1] ==0:
            if A[i] > A[i+1]:
                del A[i+1]
                del B[i+1]
                #print("A: "  +str(A) )
                #print("B: " + str(B) )
            else:
                del A[i]
                del B[i]
                #print("A: " + str(A) )
                #print("B: " + str(B) )
            i -= 1
        else:
            i += 1

    return(len(B))  
        

    pass