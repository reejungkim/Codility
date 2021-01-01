#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 12:43:23 2021

@author: reejungkim
"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        val = start
        for i in range(1, n):
            val ^= (start + 2*i)
        return val