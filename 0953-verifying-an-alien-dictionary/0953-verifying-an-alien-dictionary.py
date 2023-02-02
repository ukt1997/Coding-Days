class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        memory = {}
        for index , ch in enumerate(order):
            memory[ch] = index
        print(memory)
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if memory[words[i][j]] > memory[words[i + 1][j]]:
                        return False
                    break
        
        return True
            
        