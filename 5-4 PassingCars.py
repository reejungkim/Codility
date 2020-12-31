#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 00:11:50 2020

@author: reejungkim
"""
def solution(A):

     pairs = 0
     zero_count = 0

     for i in range(0, len(A)):
         if A[i] == 0:
             zero_count += 1
         elif A[i] == 1:
             pairs += zero_count
             if pairs > 1000000000:
                 return -1
  
     return pairs