#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:43:58 2021

@author: reejungkim
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            for i, val in enumerate(nums):
                if val > target:
                    return i 
            return len(nums)