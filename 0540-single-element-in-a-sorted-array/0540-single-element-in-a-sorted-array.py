class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) -  1
        # Only one Single value else all exactly 2 times ==> Odd no of element 
        while l <= h:
            mid = (l + h)//2
            if (mid == l == h) or (nums[mid] != nums[mid-1] and nums[mid] != nums[mid + 1]):
                # Either only one Element 
                # Both Sides are Different means mid is the single Item
                return nums[mid]
            elif nums[mid] == nums[mid - 1]:
                # Mid is paired with Previous Element 
                if ((mid - 1 ) - l ) %2 == 0:
                    # 1st Half is Even ==> Single item in 2nd Half 
                    l = mid + 1
                else:
                    h = mid - 2
            else:
                if (h - (mid + 1) ) % 2 == 0:
                    h = mid -1
                else:
                    l = mid + 2
        return -1
                                   
        