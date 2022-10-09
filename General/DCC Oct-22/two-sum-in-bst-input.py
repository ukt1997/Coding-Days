# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def load_mem(self, root):

        if (self.target - root.val) in self.mem:
            return True
        else:
            self.mem.add(root.val)

            if root.left:
                if self.load_mem(root.left):
                    return True

            if root.right:
                if self.load_mem(root.right):
                    return True
            return False

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.mem = set()
        self.target = k
        out = self.load_mem(root)
        print(out)
        return out


