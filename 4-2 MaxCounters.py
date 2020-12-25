#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 14:40:04 2020

@author: reejungkim
"""
# =============================================================================
#     
#     def solution(N, A):
#     # write your code in Python 3.6
#     
#     
#     arr = [0]*N
#     
#     
#     for i in A:
#         if i <= N:
#             arr[i-1] = arr[i-1]+1
#        
#         else: 
#             max_counter = int(max(arr))
#             arr = [max_counter]*N
#     
#         
#     return arr
#     
#     
#     pass
# =============================================================================

def solution(N, A):
    # write your code in Python 3.6
    arr = [0]*N
    
    max_counter = 0
    for i in A:
        if i <= N:
            arr[i-1] = arr[i-1]+1
            if arr[i-1] > max_counter:
                max_counter = arr[i-1]
        else: 
            arr = [max_counter]*N
        
    return arr


    pass
