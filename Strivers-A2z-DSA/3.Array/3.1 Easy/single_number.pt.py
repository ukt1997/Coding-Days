class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] ^ nums[i - 1]
        print(nums)
        return nums[len(nums) - 1]
