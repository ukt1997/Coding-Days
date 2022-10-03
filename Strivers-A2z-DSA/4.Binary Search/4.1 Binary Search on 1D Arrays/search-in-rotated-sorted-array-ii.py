class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        h = len(nums) - 1
        while (l <= h):
            mid = (l + h) // 2
            print(l, mid, h)
            if nums[mid] == target:
                return True if mid >= 0 else False
            elif nums[mid] == nums[l] == nums[h]:
                l += 1
                h -= 1
            elif nums[l] <= nums[mid]:
                print("Left is Sorted")
                if target >= nums[l] and target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                print("right is sorted")
                if target > nums[mid] and target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        return False
