# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    print(candles)
    candles_mapping = {}
    for candle in candles:
        if candle in candles_mapping.keys():
            candles_mapping[candle] += 1
        else:
            candles_mapping[candle]  = 1
    max_key = sorted(candles_mapping.keys())[len(candles_mapping.keys())-1]
    return candles_mapping[max_key]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
