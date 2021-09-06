# Enter your code here. Read input from STDIN. Print output to STDOUT

# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true 

[n,m] = input().split()
#print(n)
#print(m)

inp = input().split()
arr = [int(i)  for i in inp]
#print(arr)

like = set([int(i) for i in input().split()])
dislike = set([int(i) for i in input().split()])

count_like = sum((i in like) for i in arr )
count_dislike = sum((i in dislike) for i in arr)


#print(count_like)
#print(count_dislike)
happiness = count_like - count_dislike
print(happiness)
    

