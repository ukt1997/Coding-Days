class Solution:
    def reverseWords(self, s: str) -> str:
        cur = s.split(' ')
        print(cur)
        out = []
        for cur_str in cur:
            end = len(cur_str) - 1
            temp = ""
            while end>= 0:
                temp += cur_str[end]
                end -= 1
            out.append(temp)
        return ' '.join(out)
            
            
        
        