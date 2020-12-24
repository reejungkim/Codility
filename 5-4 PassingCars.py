#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 00:11:50 2020

@author: reejungkim
"""

def solution(A):
    # write your code in Python 3.6
    arr_0 = []
    arr_1 = []

    for i in range(0, len(A)) :
        if A[i] == 0:
            arr_0.append(i)
        else:
            arr_1.append(i)



    count = 0

    for x in arr_0:
        for y in arr_1:
            if x < y:
                count +=1
     
    if count > 1000000000:
        solution = -1
    else:
        solution = count

    return solution
   

#    return -1


    pass