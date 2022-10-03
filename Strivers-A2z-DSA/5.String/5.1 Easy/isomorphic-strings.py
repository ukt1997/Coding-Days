class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_arr = [-1 for i in range(128)]
        memory = [-1 for i in range(128)]
        for i in range(len(s)):
            if map_arr[ord(s[i])] == -1 and memory[ord(t[i])] == -1:
                memory[ord(t[i])] = 1
                map_arr[ord(s[i])] = t[i]
            else:
                expected_t = map_arr[ord(s[i])]
                if expected_t != t[i]:
                    return False
        return True

