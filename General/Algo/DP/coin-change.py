# https://www.hackerrank.com/challenges/coin-change/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    arr = [[-1 for i in range(n+1)]  for i in range(len(c))]
    sorted_c = sorted(c)
    for i in range(len(sorted_c)):
        arr[i][0] = sorted_c[i]
        
    for i in range(len(sorted_c)):
        cur_num = arr[i][0]
        for j in range(1,n+1):
            if j==cur_num:
                arr[i][j] = 1
                if i>0 and arr[i-1][j] > -1:
                    arr[i][j] += arr[i-1][j]
            elif j > cur_num:
                # we are Not Taking it 
                if i> 0 and arr[i-1][j] > -1:
                    arr[i][j] = arr[i-1][j]
                # we took it 
                if arr[i][j-cur_num] > -1 :
                    arr[i][j] = max(arr[i][j],0)
                    arr[i][j] += arr[i][j-cur_num]
            else:
                if i> 0:
                    arr[i][j] = arr[i-1][j]
    print([i for i in range(n)])
    for i in arr:
        print(i)
    return max(arr[len(sorted_c)-1][n],0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
