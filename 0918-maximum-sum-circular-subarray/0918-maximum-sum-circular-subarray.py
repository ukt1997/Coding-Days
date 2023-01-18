class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ret = nums[0]
        total = sum(nums)
        maxtotal, mintotal = nums[0], 0
        for num in nums[1:]:
            print(maxtotal, mintotal)
            maxtotal = max(num, num + maxtotal)
            mintotal = min(num, num + mintotal)
            ret = max(ret, maxtotal, total - mintotal)
        return ret
        