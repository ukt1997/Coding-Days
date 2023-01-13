# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ret = []
        self.stack = []
        if root:
            # Starting Stack with Root Node 
            self.stack.append([root])
            while len(self.stack):
                # Pop 1st level list of nodes and Add all the childs of all these Nodes
                cur = self.stack.pop(0)
                temp = []
                nextchilds = []
                for  node in cur:
                    # And While Processing keep adding values of all the nodes of cur Level 
                    temp.append(node.val)
                    if node.left : nextchilds.append(node.left)
                    if node.right : nextchilds.append(node.right)
                if temp:
                    # Append the value list in Output
                    self.ret.append(temp)
                if nextchilds:
                    # Add childs of last level as a new level
                    self.stack.append(nextchilds)
                    
        
        return self.ret
            
        
        