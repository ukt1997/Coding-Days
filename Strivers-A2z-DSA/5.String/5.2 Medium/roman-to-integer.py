class Solution:
    mem = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        last_add = 0
        total = 0
        for cur in s[::-1]:
            cur_val = self.mem[cur]
            if cur_val >= last_add:
                total += cur_val
            else:
                total -= cur_val
            last_add = cur_val

        return total

