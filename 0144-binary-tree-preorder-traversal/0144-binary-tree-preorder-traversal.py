# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Pre Order Means Order will be : Root - Left - Right 
        stack = []
        ret = []
        if root:
            stack.append(root)
            while stack:
                cur = stack.pop()
                ret.append(cur.val)
                print(ret)
                if cur.right: stack.append(cur.right)
                if cur.left: stack.append(cur.left)
        return ret
            
            
        