class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memory = set()
        for num in nums:
            memory.add(num)

        print(memory)

        max_streak = 0

        for num in nums:
            if (num - 1 not in memory):
                # this num is 1st of cur Streak
                cur_num = num
                streak = 1
                while (cur_num + 1 in memory):
                    # cheicking for all consecutive Elements
                    cur_num = cur_num + 1
                    streak += 1
                max_streak = max(max_streak, streak)
        return max_streak


