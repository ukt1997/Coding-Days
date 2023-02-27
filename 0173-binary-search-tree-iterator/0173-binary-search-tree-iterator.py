# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        arr = []
        def inOrder(node):
            if node:
                if node.left:
                    inOrder(node.left)
                arr.append(node.val)
                if node.right:
                    inOrder(node.right)
        inOrder(root)
        self.mem = arr
        self.cur = -1
        

    def next(self) -> int:
        self.cur += 1
        return self.mem[self.cur]
    
        

    def hasNext(self) -> bool:
        return (self.cur + 1 < len(self.mem))
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()