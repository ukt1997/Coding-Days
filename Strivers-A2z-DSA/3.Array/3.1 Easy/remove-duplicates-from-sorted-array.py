class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ret = 1
        for i in nums:
            if i > nums[ret - 1]:
                nums[ret] = i
                ret += 1
        return ret

