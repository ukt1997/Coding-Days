# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if root:
            if root.left:
                temp = self.postorderTraversal(root.left)
                if temp : ret.extend(temp) 
            if root.right:
                temp = self.postorderTraversal(root.right)
                if temp : ret.extend(temp)
            ret.append(root.val)
        
        return ret
        