# https://www.hackerrank.com/challenges/swap-nodes-algo/problem?isFullScreen=true

# Need Some Improvement as 2 test Case Failed due to Maximum Recursssion Limit 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
class Node:
    def __init__(self,info):
        self.info = info
        self.right = None
        self.left = None
    
    def __str__(self):
        return self.info

def create_tree(indexes,val):
    n = Node(val)
    cur_val = indexes[val-1]
    if cur_val[0] != -1:
        n.left = create_tree(indexes,cur_val[0])
    if cur_val[1] != -1:
        n.right = create_tree(indexes,cur_val[1])
    return n

def in_order(node,out):
    if node is None:
        return
    in_order(node.left,out)
    #print(node.info,end = " ")
    out.append(node.info)
    in_order(node.right,out)
    return

def map_depth(node,l,m):
    if node is None:
        return
    if l not in m.keys():
        m[l] = [node]
    else:
        m[l].append(node)
    map_depth(node.left,l+1,m)
    map_depth(node.right,l+1,m)
    return 
    
 
def swapNodes(indexes, queries):
    # Write your code here
    Head = create_tree(indexes , 1)
    m = {}
    map_depth(Head,1,m)
    """for i in m.keys():
        print("Key ",i)
        for j in m[i]:
            print(j.info)"""
    max_depth = max(m.keys())
    ret = []
    for i in queries:
        cnt = 1
        while cnt*i <= max_depth:
            cur_depth = cnt*i
            for nodes in m[cur_depth]:
                temp = nodes.right
                nodes.right = nodes.left
                nodes.left = temp
            cnt += 1
        out = []
        in_order(Head,out)
        #print(out)
        ret.append(out)
    
    return ret
            
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
