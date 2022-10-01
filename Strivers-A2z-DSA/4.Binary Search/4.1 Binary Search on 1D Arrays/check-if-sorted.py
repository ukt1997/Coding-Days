# User function Template for python3
# Not a BS Question

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        ret = 1
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                ret = 0
        return ret


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends