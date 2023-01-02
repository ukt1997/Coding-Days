class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        min = 1
        max = 1
        for i in range(1,len(word)):
            val = ord(word[i])
            if i == 1:
                min = val
                max = val
            elif val < min:
                min = val
            elif val > max:
                max = val 

        if (min >= 65 and max <=90 and ord(word[0]) >= 65 and ord(word[0]) <= 90) or (min>= 97 and max <= 122 ):
            return True
        elif len(word) == 1:
            return True
        else:
            return False
