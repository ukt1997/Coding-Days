# https://www.hackerrank.com/challenges/morgan-and-a-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'morganAndString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def morganAndString(a, b):
    # Write your code here
    out = ""
    out_size = len(a) + len(b)
    a += 'z'
    b += 'z'
    while len(out) < out_size:
        if len(a) == 0:
            out += b
        elif len(b) == 0:
            out += a
        elif a[0]>b[0]:
            out += b[0]
            b = b[1:]
        elif a[0]<b[0]:
            out += a[0]
            a = a[1:]
        elif a > b :
            out += b[0]
            b = b[1:]
        elif a <= b :
            out += a[0]
            a = a[1:]
        #print(out + " "+a+" "+b)
            
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
