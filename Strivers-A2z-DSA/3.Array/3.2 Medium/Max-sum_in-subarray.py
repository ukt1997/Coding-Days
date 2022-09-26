# User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr, N):
        # Your code goes here
        max_sum = arr[0] + arr[1]
        for i in range(2, N):
            if arr[i] + arr[i - 1] > max_sum:
                max_sum = arr[i] + arr[i - 1]
        return max_sum


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.pairWithMaxSum(a, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends