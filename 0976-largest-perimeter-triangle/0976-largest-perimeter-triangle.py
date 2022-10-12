class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        print(nums)
        while len(nums) > 2 and (nums[0] >= nums[1] + nums[2]):
            nums.pop(0)
        if len(nums) <= 2:
            return 0
        else:
            return nums[0] + nums[1] + nums[2]
        
        