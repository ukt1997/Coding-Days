class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_of_words = s.split(' ')
        ret = True
        memory_char = {}
        memory_word = {}
        if len(pattern) != len(list_of_words):
            return False
        for i in range(len(pattern)):
            cur_char = pattern[i]
            cur_word = list_of_words[i]
            if cur_char not in memory_char and cur_word not in memory_word:
                memory_char[cur_char] = cur_word
                memory_word[cur_word] = cur_char
            elif cur_char not in memory_char:
                ret = False
            elif cur_word not in memory_word:
                ret = False
            elif memory_char[cur_char] != cur_word or memory_word[cur_word] != cur_char:
                ret = False 
        return ret


