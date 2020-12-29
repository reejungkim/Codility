#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 01:10:52 2020

@author: reejungkim
"""

class Solution:
    def reverse(self, x: int) -> int:
        
        x= str(x)
        length = len(x)
        num_reversed = ''
        
        for i in range(0, length):
            num = x[length-1 - i]
            num_reversed += num
            

        if num_reversed[-1]=='-':
            num_reversed = -int(num_reversed[:-1])
        else:
            num_reversed = int(num_reversed)
        
        if -(2**31) <= num_reversed <= ((2**31) - 1):
            return num_reversed
        else:
            return 0