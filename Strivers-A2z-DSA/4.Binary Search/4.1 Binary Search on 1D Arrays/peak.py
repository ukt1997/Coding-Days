class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            left = 0
            right = 0
            if mid == 0 or nums[mid] > nums[mid - 1]:
                left = 1
            if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
                right = 1
            print(start, end, mid)

            if left + right == 2:
                return mid
            elif nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1
        return -1
