class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        mem = {}
        ret = 0
        for item in tasks:
            if item in mem:
                mem[item] += 1
            else:
                mem[item] = 1
        for key in mem:
            #print(key,mem[key])
            if mem[key] % 3 == 0:
                ret += mem[key]//3
            elif mem[key] % 3 == 2:
                ret += (mem[key]//3 + 1)
            elif mem[key]%3 == 1 and mem[key]//3 > 0:
                ret += (mem[key]//3 + 1)
            else:
                return -1    
        return ret
        