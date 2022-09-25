class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p_nums = [i for i in nums if i >= 0]
        n_nums = [i for i in nums if i < 0]
        for i in range(len(n_nums)):
            nums[2 * i + 1] = n_nums[i]
            nums[2 * i] = p_nums[i]
        return nums



