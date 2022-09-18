# https://www.hackerrank.com/challenges/almost-sorted/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    #print(arr)
    #print(sorted(arr))
    arr1 = sorted(arr)
    diff_indices = [] # To Store Indices Where values are Not Matching 
    for i in range(len(arr)):
        if arr[i] != arr1[i]:
            diff_indices.append(i)
    #print(diff_indices)
    if len(diff_indices) == 2 : # if only 2 index values are Diff Then we can Swap 
        print('yes')
        print('swap '+str(diff_indices[0]+1)+' '+str(diff_indices[1]+1))
    else: # Else we have to Check Can We sort by Revershing a Sub Array 
        chk = True
        diff = len(diff_indices)
        #print(diff/2)
        for i in range(math.ceil(diff/2)):
            #print('i = ',i)
            #print(arr[diff_indices[i]])
            #print(arr1[diff_indices[diff-1-i]])
            if arr[diff_indices[i]] != arr1[diff_indices[diff-1-i]]:
                #print(arr[diff_indices[i]] , arr1[diff_indices[diff-1-i]])
                chk = False
        if chk:
            print('yes \nreverse '+str(diff_indices[0]+1)+ ' ' +str(diff_indices[diff-1]+1) )
        else:
            print('no')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
