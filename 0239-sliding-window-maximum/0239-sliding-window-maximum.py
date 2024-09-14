import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        #print(d)
        out = []    
        for i , n in enumerate(nums):
            while d and nums[d[-1]] <  n:
                d.pop()
                #print("Pop from Queue" , d )
            
            d.append(i)
            
            if i - k == d[0]:
                d.popleft()
                # it is out of window now 
            if i >= k - 1:
                out.append(nums[d[0]]) # adding top Element to List 
            #print(d)
        return out
        