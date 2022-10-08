class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split(" ")
        print(li)
        out = reversed([i for i in li if i != ''])
        return " ".join(out)
