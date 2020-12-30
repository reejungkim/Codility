#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 20:46:30 2020

@author: reejungkim
"""

def solution(A):
    missing_int = 0
    for value in A:
        missing_int ^= value
        
    return missing_int