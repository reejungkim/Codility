#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:54:47 2020

@author: reejungkim
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")



#Complexity : O(N**2)

def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 0
    else: 
        return findMaxProfit(A)

    pass


def findMaxProfit(A):
    arr = []

    for i in range(len(A)-1):
        #print(i)
        p_buy = A[i]
        if p_buy <0:
            p_buy = p_buy*-1
        
        p_sell = max(A[i+1:])
        profit = p_sell - p_buy
        arr.append(profit)
        #print(arr)
    
    max_profit = max(arr)
    if max_profit <= 0 :
        return 0
    else:
        return max_profit

pass