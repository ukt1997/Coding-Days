class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        chk = 0
        for i in range(1, n + 1):
            if nums[i % n] < nums[(i - 1) % n]:
                chk += 1
        if chk <= 1:
            return True
        else:
            return False
