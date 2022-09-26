class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_v = nums[0]
        cur_v = nums[0]
        for i in range(1, len(nums)):
            if nums[i] + cur_v < nums[i]:
                cur_v = nums[i]
            else:
                cur_v += nums[i]
            if max_v < cur_v:
                max_v = cur_v
            print(cur_v)
        return max_v

