class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        n = len(s)
        for i in range(n):
            if goal == s[i + 1:] + s[:i + 1]:
                return True
        return False
