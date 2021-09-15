# https://www.hackerrank.com/challenges/equal/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    # Write your code here
    in_min_val = min(arr)
    cnt_list = []
    for j in range(5):
        min_val = in_min_val - j
        cnt = 0
        for i in arr:
            cur = i
            if cur != min_val:
                diff = cur - min_val
                if diff >= 5:
                    cnt += diff//5
                    diff = diff%5
                if diff >= 2:
                    cnt += diff//2
                    diff = diff%2
                if diff > 0:
                    cnt += diff
                    diff = 0
        cnt_list.append(cnt)
    print(cnt_list)       
    return min(cnt_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
