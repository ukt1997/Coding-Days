class Solution:
    def frequencySort(self, s: str) -> str:
        mem = [0 for i in range(125)]

        for i in s:
            index = ord(i)
            mem[index] += 1

        sorted_mem = reversed(sorted([[i, mem[i]] for i in range(125) if mem[i] > 0], key=lambda x: x[1]))
        ret = ''
        for cur in sorted_mem:
            #print(cur)
            val = cur[1]
            index = cur[0]
            #print(val)
            #print(index)
            for i in range(val):
                ret += chr(index)

        return ret
