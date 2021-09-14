# https://www.hackerrank.com/challenges/sherlock-and-anagrams/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
    
def sherlockAndAnagrams(s):
    # Write your code here
    sub_str_s = [''.join(sorted(s[i:j])) for i in range(len(s))
                            for j in range(i+1,len(s)+1)]
    #print(sub_str_s)
    
    count = 0
    result = {}
    
    for st in sub_str_s:
        if st in result.keys():
            result[st] += 1
        else:
            result[st] = 1
    
    #print(result)
    
    for key in result.keys():
        val = result[key]
        count += (val*(val-1))//2
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
