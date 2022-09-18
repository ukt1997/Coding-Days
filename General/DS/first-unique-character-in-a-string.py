#https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        mem = [0]*26
        for i in s:
            mem[ord(i)-ord('a')] += 1
        print(mem)
        for i in range(len(s)):
            if mem[ord(s[i])-ord('a')] == 1:
                return i
        return -1
        