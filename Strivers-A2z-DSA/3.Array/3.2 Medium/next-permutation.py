#https://leetcode.com/problems/next-permutation/submissions/
class Solution:
    def reverseList(self, nums: List[int], left: int, right: int) -> None:
        while right > left:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            right -= 1
            left += 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breakpoint = -1
        n = len(nums)
        for i in reversed(range(n - 1)):
            if nums[i] < nums[i + 1]:
                breakpoint = i
                break
        left = 0
        right = n - 1
        if breakpoint >= 0:
            for i in reversed(range(n)):
                if nums[i] > nums[breakpoint]:
                    temp = nums[i]
                    nums[i] = nums[breakpoint]
                    nums[breakpoint] = temp
                    break
            left = breakpoint + 1
            rignt = n - 1
        self.reverseList(nums, left, right)

