def check(memory):
        for i in memory:
            if i!= 0:
                return False
        return True

class Solution:
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        
        if m>n:
            return False
        
        start = 0
        end = m-1
        
        memory = [0]*26
        for i in s1:
            memory[ord(i)-ord('a')] -= 1
        print(memory)
        for i in range(m):
            memory[ord(s2[i])-ord('a')] += 1
        print(memory)
        print(sum(memory))
        if check(memory):
            return True
        else:
            for i in range(n-m):
                memory[ord(s2[i])-ord('a')] -= 1
                memory[ord(s2[m+i])-ord('a')] += 1
                if check(memory):
                    return True
        return False
                
            
        
        