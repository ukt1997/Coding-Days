# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ret = 0
        if root :
            ret = 1
            ret += max(self.maxDepth(root.left) if root.left else 0 , self.maxDepth(root.right) if root.right else 0)
        return ret
        
        