# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Pre Order Means Order will be : Root - Left - Right 
        if root:
            ret = [root.val]
            if root.left:
                L = self.preorderTraversal(root.left)
                ret.extend(L)
            if root.right:
                R = self.preorderTraversal(root.right)
                ret.extend(R)
            return ret
        else:
            return []
            
            
        