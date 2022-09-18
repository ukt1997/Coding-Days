# User function Template for python3
class Solution:

    def print2largest(self, arr, n):
        # code here
        max_val = arr[0]
        max_2 = -1
        for i in arr:
            if i > max_val:
                max_2 = max_val
                max_val = i
            elif i > max_2 and i < max_val:
                max_2 = i
        return max_2


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends