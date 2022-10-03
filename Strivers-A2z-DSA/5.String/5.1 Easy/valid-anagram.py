def check(memory):
    for i in memory:
        if i != 0:
            return False
    return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memory = [0] * 26
        for i in s:
            memory[ord(i) - ord('a')] -= 1
        print(memory)
        for i in t:
            memory[ord(i) - ord('a')] += 1
        print(memory)
        return check(memory)
