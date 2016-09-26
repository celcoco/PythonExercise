#!/bin/python

import sys

arr = []
arr_tmp = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
maxsum = 0
tmp = 0
for i in xrange(4):
    for j in xrange(4):
        #tmp = sum(arr[i][j:j+2])
        tmp = sum(arr[i][j:j+2],arr[i+2][j:j+2],arr[i+1][j+1])
        #print maxsum
        if tmp > maxsum:
            maxsum = tmp
print maxsum