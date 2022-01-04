class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zero_count = 0
        n = len(nums)
        while i + zero_count < n:
            #print(i)
            if nums[i] == 0:
                nums.pop(i)
                zero_count += 1
                #n -= 1
            else:
                i += 1
            #print(nums)
        for i in range(zero_count) :
            nums.append(0)
    
                    
        