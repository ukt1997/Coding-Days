class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        arr = [0 for i in range(26)]
        for i in sentence:
            arr[ord(i) - ord('a')] = 1
        print(arr)
        return True if sum(arr) == 26 else False
        