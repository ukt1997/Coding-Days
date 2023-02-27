# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        par = (len(nums))// 2
        #print(nums[head])
        head = TreeNode(nums[par])
        if par > 0:
            head.left = self.sortedArrayToBST(nums[:par])
        if par < len(nums) - 1:
            head.right = self.sortedArrayToBST(nums[par+1:])
        return head