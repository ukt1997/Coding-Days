class Solution:
    def myAtoi(self, s: str) -> int:
        # return 12
        n = len(s)
        start = 0

        # Removed all Leading <Spaces>
        positive = True
        while start < n and s[start] == ' ':
            start += 1

        # Checking if -ve Number
        if start < n and s[start] == '-':
            # print(start," Here - ")
            positive = False
            start += 1
            if start < n and (s[start] < '0' or s[start] > '9'):
                return 0
        elif start < n and s[start] == '+':
            # print(start," Here + ")
            start += 1
            # print(s[start])
            if start < n and (s[start] < '0' or s[start] > '9'):
                return 0
        elif start < n and (s[start] < '0' or s[start] > '9'):
            print(start, " Here return ")
            return 0

        end = start
        while end < n and s[end] >= '0' and s[end] <= '9':
            end += 1

        # print(start,end)
        if start < n:
            val = int(s[start])
            for i in range(start + 1, end):
                val = val * 10 + int(s[i])
                print(val)
            if positive:
                return min(val, 2147483647)
            else:
                return max(-1 * val, -2147483648)

        return 0




