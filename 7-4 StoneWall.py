#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 21:19:49 2020

@author: reejungkim
"""


def solution(H):
    count = 0
    #height = 0
    height_arr = [0]

    for i in range(len(H)):
        while H[i] < height_arr[-1]:
            height_arr.pop()
        if H[i] > height_arr[-1]:
            height_arr.append(H[i])
            count +=1
        if H[i] < height_arr[-1]:
            height_arr.append(H[i])
            count +=1

    return count
pass