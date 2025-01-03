#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:00:42 2020

@author: reejungkim
"""

'''
https://codility.com/media/train/1-TimeComplexity.pdf

But the third person’s solution is even quicker. Let us write the sequence 1, 2, . . . , n and
repeat the same sequence underneath it, but in reverse order. Then just add the numbers
from the same columns:
1 2 3 . . . n − 1 n
n n − 1 n − 2 . . . 2 1
n + 1 n + 1 n + 1 . . . n + 1 n + 1
The result in each column is n + 1, so we can easily count the final result:
3.9: Model solution — time complexity O(1).
1 def model_solution(n):
2 result = n * (n + 1) // 2
3 return result

'''

def solution(A):
    # write your code in Python 3.6
    total = sum(A)
    total_expected = (len(A)+2) * (len(A)+1) //2

    return total_expected - total

    pass