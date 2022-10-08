class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_val = s[0]
        max_len = 1
        for i in range(n):
            for j in range(i + 1, n):
                chk = True
                start = i
                end = j
                # print(start,end)
                while start < end:
                    # print("In Loop ",start , end)
                    if s[start] != s[end]:
                        chk = False
                    start += 1
                    end -= 1
                if chk and max_len < (j - i + 1):
                    # print("Inside IF check")
                    max_len = j - i + 1
                    max_val = s[i:j + 1]
        return max_val





