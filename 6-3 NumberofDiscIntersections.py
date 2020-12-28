#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 00:42:10 2020

@author: reejungkim
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
   
    arr=[]
    for i, radius in enumerate(A):
        arr.append((i - radius, -1)) #'opening'))
        arr.append((i + radius, 1)) #'closing'))

    arr = sorted(arr)
    #print(arr)

    intersections = 0
    circle_count = 0
    for i, option in enumerate(arr):
        #print(i)
        if option[1]==1: #'closing': #closing 
            circle_count -= 1
        if option[1]==-1: #'opening': #opening
            intersections += circle_count
            circle_count +=1  # a disc is opened(started)
            #print('opening' + str(intersections))


    #print(intersections)   
    if intersections > 10000000:
        return -1
    else:
        return intersections 


    pass