#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        sorted_li = nums  # sorted(nums)

        # print(sorted_li)

        start_diff = abs(target - (nums[0] + nums[1] + nums[2]))
        closest_sum = nums[0] + nums[1] + nums[2]
        if closest_sum == target:
            return closest_sum

        # print("start_diff ",start_diff)
        # print("closest_sum ",closest_sum)

        for i in range(n - 2):
            # print(" 1st Val = ",sorted_li[i])
            start = i + 1
            end = n - 1
            while start < end:
                sum_cur = sorted_li[i] + sorted_li[start] + sorted_li[end]
                # print(start,end , " Sum_cur = ",sum_cur)
                if sum_cur == target:
                    return sum_cur

                if target < sum_cur:
                    if start_diff > abs(target - sum_cur):
                        start_diff = abs(target - sum_cur)
                        closest_sum = sum_cur
                    end -= 1
                else:
                    if start_diff > abs(target - sum_cur):
                        start_diff = abs(target - sum_cur)
                        closest_sum = sum_cur
                    start += 1

        return closest_sum