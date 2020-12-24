#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:10:09 2020

@author: reejungkim
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#5-3 MinTwoSlice

def solution(A):
    # write your code in Python 3.6
    dict = {}

    for x in range(0, len(A)):
        for y in range(x+1, len(A)):
            avg = sum(A[x:y+1])/len(A[x:y+1])
            print(A[x:y+1])
            print("length of array: " + str(len(A[x:y+1])))
            print("avg" + str(avg))

            dict[(x,y)]=avg
    print(dict)
    #print(dict.values())
    #print(len(dict))

    min_avg = min(dict.values())
    print(min_avg)
    #print(dict.keys())

    for key in dict.keys():
        if dict[key] == min_avg:
            #print("answer"+str(key))
            #print(key[0])
            solution = key[0]


    return solution 

    pass