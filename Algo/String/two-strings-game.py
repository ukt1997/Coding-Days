# https://www.hackerrank.com/challenges/two-strings-game/problem 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. LONG_INTEGER k
#  2. STRING a
#  3. STRING b
#

def twoStrings(k, a, b):
    # Write your code here
    all_sub_a = [a[i: j] for i in range(len(a)) for j in range(i+1, len(a) + 1)]
    all_sub_a.append('')
    print(sorted(all_sub_a))
    all_sub_b = [b[i: j] for i in range(len(b)) for j in range(i+1, len(b) + 1)]
    all_sub_b.append('')
    print(sorted(all_sub_b))
    
    return['a','c']

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    a = input()

    b = input()

    result = twoStrings(k, a, b)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
