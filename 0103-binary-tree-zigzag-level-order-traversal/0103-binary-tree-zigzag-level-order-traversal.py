# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.out  = []
        self.order = 1
        
        def getNextLevel(par):
            ret = []
            outCur = []
            
            for node in par:
                if node is None:
                    continue
                if node.left:
                    ret.append(node.left)
                    outCur.append(node.left.val)
                if node.right:
                    ret.append(node.right)
                    outCur.append(node.right.val)
                    
            if self.order : outCur.reverse()
                
            if len(outCur) :
                self.out.append(outCur)
                
            self.order += 1
            self.order = self.order % 2
            
            return ret
        
        par = [root]
        if root: self.out.append([root.val])
        while par:
            par = getNextLevel(par)
        return self.out
        
                
        