# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if root:
            if root.left:
                temp = self.inorderTraversal(root.left)
                if temp : ret.extend(temp) 
            ret.append(root.val)
            if root.right:
                temp = self.inorderTraversal(root.right)
                if temp : ret.extend(temp)
        
        return ret