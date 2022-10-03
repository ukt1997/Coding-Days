# https://leetcode.com/problems/largest-odd-number-in-string/submissions/
class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)

        for i in range(n, 0, -1):
            if int(num[i - 1]) % 2 != 0:
                return num[:i]
        return ""
