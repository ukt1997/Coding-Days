class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        count = 0
        max_count = 0
        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1

            if count > max_count:
                max_count = count
        return max_count

