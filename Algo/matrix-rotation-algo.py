# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Write your code here
    #print(matrix)
    m = len(matrix)
    n = len(matrix[0])
    no_of_layers = (min(m,n))//2
    #print(no_of_layers)
    
    layers = []
    # Building Layers For Rotation 
    for i in range(no_of_layers):
        cur = []
        cur.extend(matrix[i][i:n-i])
        #print(cur)
        cur.extend([li[n-1-i] for li in matrix[i+1:-1*(i+1)]] )
        #print(cur)
        cur.extend(reversed(matrix[m-1-i][i:n-i]))
        #print(cur)
        cur.extend(reversed([li[i] for li in matrix[i+1:-1*(i+1)]]) )
        #print(cur)
        layers.append(cur)
    #print(layers)
    
    #Rotating Layers 
    for i in range(no_of_layers):
        cur_r = r%(len(layers[i]))
        cur = layers[i][cur_r:]
        cur.extend(layers[i][:cur_r])
        layers[i] = cur
    #print(layers)
    
    #Restoring Matrix From Rotated Layers 
    for i in range(no_of_layers):
        matrix[i][i:n-i] = layers[i][0:n-2*i]
        cur = layers[i][n-2*i:]
        layers[i] = cur 
        #print(layers[0])
        for j in range(i+1,m-1-i):
            matrix[j][i] = layers[i].pop()
            matrix[j][n-1-i] = layers[i].pop(0)
        matrix[m-1-i][i:n-i] = reversed(layers[i][0:n-2*i])
    for i in matrix:
        for j in i:
            print(j, end = " ")
        print()
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
