#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 23:11:29 2020

@author: reejungkim
"""

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums)==2:
            return [0,1]
        else:
            for i, val in enumerate(nums):
                arr=nums[:]
                del arr[i]
                if target - val in arr:
                    return [i, nums.index(target-val, i+1)]
