class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        if target < nums[start]:
            return 0
        elif target > nums[end]:
            return end + 1

        while start <= end:
            print(start, end)
            mid = (start + end) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
                mid = start
            elif nums[mid] > target:
                end = mid - 1
        return mid

