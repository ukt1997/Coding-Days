# https://www.hackerrank.com/challenges/maximize-it/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

inp=  input().split()
k,m = int(inp[0]),int(inp[1])

#print(k,m)

arr = []
for i in range(k):
    cur = input().split()
    cur1 = [(int(c)**2)%m for c in cur[1:]]
    arr.append(cur1)
#print(arr)


print(max(map(lambda x: sum(x)%m, product(*arr))))    