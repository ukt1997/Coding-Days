# cook your dish here
# https://www.codechef.com/problems/ZEROONE
t = int(input())
for cur in range(t):
    n = int(input())
    zeros = []
    ones = []
    inp = input().split()
    for i in range(n):
        if i%2 == 0:
            zeros.append(int(inp[i]))
        else:
            ones.append(int(inp[i]))
            
    zeros_s = sorted(zeros)[::-1]
    ones_s = sorted(ones)
    #print(zeros)
    #print(ones)
    #print(zeros_s)
    #print(ones_s)
    out = []
    Z_c = 0
    O_c = 0
    out_C = 0
    res = 0
    for i in range(n):
        if i%2 == 0:
            out.append(zeros_s[Z_c])
            out_C += zeros_s[Z_c]
            Z_c += 1
        else:
            out.append(ones_s[O_c])
            res += out_C*ones_s[O_c]
            O_c += 1 
    #print(out)
    for i in out[:-1]:
        print(i,end = " ")
    print(out[-1])
    print(res)
    