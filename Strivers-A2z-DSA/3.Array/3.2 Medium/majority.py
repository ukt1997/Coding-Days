# https://leetcode.com/problems/majority-element/submissions/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        count_max = 1
        majority_val = sorted_list[0]
        count_cur = 1
        for i in range(1,len(nums)):
            if sorted_list[i] == sorted_list[i-1]:
                count_cur += 1
            else:
                count_cur = 1
            if count_max  < count_cur:
                count_max = count_cur
                majority_val = sorted_list[i]
        return majority_val