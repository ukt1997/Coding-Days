# User function Template for python3

class Solution:

    # Function to return a list containing the union of the two arrays.
    def mergeArrays(self, a, b, n, m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here
        out = []
        i = 0
        j = 0
        cnt = -1
        while i < n and j < m:
            if a[i] < b[j]:
                if cnt < 0:
                    out.append(a[i])
                    cnt += 1
                elif cnt >= 0 and a[i] > out[cnt]:
                    out.append(a[i])
                    cnt += 1
                i += 1
            else:
                if cnt < 0:
                    out.append(b[j])
                    cnt += 1
                elif cnt >= 0 and b[j] > out[cnt]:
                    out.append(b[j])
                    cnt += 1
                j += 1

        if j < m:
            for cur in b[j:]:
                if cur > out[cnt]:
                    out.append(cur)
                    cnt += 1
        if i < n:
            for cur in a[i:]:
                if cur > out[cnt]:
                    out.append(cur)
                    cnt += 1
        return out


# {
# Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, m = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.mergeArrays(a, b, n, m)
        for val in li:
            print(val, end=' ')
        print()
# } Driver Code Ends