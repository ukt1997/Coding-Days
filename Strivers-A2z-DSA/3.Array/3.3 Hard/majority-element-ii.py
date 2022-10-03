# https://leetcode.com/problems/majority-element-ii/
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        temp_list = sorted(nums)
        print(temp_list)
        ret = []
        min_count = len(nums) / 3
        cur = temp_list[0]
        count = 1
        for i in range(1, len(nums)):
            print(i, temp_list[i])
            if temp_list[i] == cur:
                count += 1
            elif count > min_count:
                ret.append(cur)
                cur = temp_list[i]
                count = 1
            else:
                cur = temp_list[i]
                count = 1
        if count > min_count:
            ret.append(cur)
        return ret

