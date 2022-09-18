class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """ Solution - 1  Space : O(1) -- K*N (TLE) 
        n = len(nums)
        #print(nums)
        #print(n)
        for i in range(k):
            #print("i = ",i)
            cur = nums[n-1]
            for j in range(n-2,-1,-1):
                #print("j = ",j)
                nums[j+1] = nums[j]
            nums[0] = cur
            #print(nums)
        """
        """ 2nd Solution Not Working 
        n = len(nums)
        temp = [i for i in nums]
        nums = temp[-k:]
        print(nums)
        for num in temp[0:n-k]:
            nums.append(num)
        print(nums)
        #nums = [i for i in out]
        """
        n = len(nums)
        for i in range(k):
            cur = nums[n - 1]
            nums.pop()
            nums.insert(0, cur)
            # print(nums)



