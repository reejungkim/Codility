#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:32:35 2020

@author: reejungkim
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(S):
    # write your code in Python 3.6
    arr = []
    dict = {
        "{":"}", 
        "}":"{",
        "[":"]",
        "]":"[" ,
        "(":")", 
        ")":"(", 
    }

    
    if S == "":
        solution =1
    #elif len(S) % 2 == 1:
    #    solution = 0
    else:
        mid = int(len(S)/2) 
        #print(mid)
        #print(len(S))
        for i in range(0, mid+1):
            #print("left:" + dict[S[i] ] )
            #print("right:" + S[len(S)-1-i]) 
            if S[i] in list(dict.keys()):
                left = dict[S[i]]
                right = S[len(S)-1-i]
            else: 
                left = S[i]
                right = S[len(S)-1-i]
            
                x = 1
            if str(left) == str(right): #S[i] == S[len(S)-1-i]:
                x = 1 #propeer
            else:
                x = 0 #not porper
            arr.append(x)  
        #not proper if any of the item is not properly nested
        solution = min(arr) 

    return solution

    pass