class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #print(nums1)
        #print(nums2)
        while n> 0:
            #print(m,n)
            #print(nums1)
            if m==0:
                nums1[m+n-1] = nums2[n-1]
                n-= 1
            elif nums2[n-1]>=nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1 
            else:
                nums1[m+n-1] = nums1[m-1]
                m-= 1
        print(nums1)
            
        