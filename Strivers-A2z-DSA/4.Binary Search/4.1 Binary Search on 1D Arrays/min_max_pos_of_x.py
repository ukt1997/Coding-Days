class Solution:

    def maxpos(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid < len(nums) - 1 and nums[mid + 1] == target:
                    start = mid + 1
                else:
                    return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def minpos(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid > 0 and nums[mid - 1] == target:
                    end = mid - 1
                else:
                    return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.minpos(nums, target), self.maxpos(nums, target)]

