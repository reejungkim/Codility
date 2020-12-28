#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:08:43 2020

@author: reejungkim
"""



def solution(S, P, Q):
    # write your code in Python 3.6
    dict = {'A':1, 'C':2, 'G':3, 'T':4}
    S_converted = []
    arr = []

    for i in S:
        S_converted.append(dict[i])

    for i in range(0, len(P)):
        start = P[i]
        end = Q[i]
        arr.append(min(S_converted[start: end+1]))

    return arr

    
    pass


# def solution(S, P, Q):
#     # write your code in Python 3.6
#     dict = {'A':1, 'C':2, 'G':3, 'T':4}
    
#     arr = []

#     for i in range(0, len(P)):
#         start = P[i]
#         end = Q[i]
#         #print(S[start: end+1])
#         S_converted = []
#         for n in S[start: end+1]:
#             S_converted.append(dict[n])
#             #print(S_converted)
#         arr.append(min(S_converted))

#     return arr



#     pass