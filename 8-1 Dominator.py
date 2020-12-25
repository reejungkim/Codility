#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 00:01:52 2020

@author: reejungkim
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    half = len(A)/2
    dict = {}
    #arr = []

    for i in set(A):
        count = A.count(i)
        dict[i] = count
        max_count = max( dict.values())
    
    #print(dict)
    #print( max_count )
    for key in dict.keys():
        if dict[key] == max_count:
            dominator = key


    for i in range( len(A) ):
        if A[i] ==  dominator:
            answer = i
            #arr.append(i)

    if len(A)==0:
        solution = -1
    elif max_count <= half:
        solution = -1
    else: 
        solution = answer #arr

    


    return solution

    pass