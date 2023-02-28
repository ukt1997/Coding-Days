# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        visited = {}
        
        def traverse(root: Optional[TreeNode]) -> int:
            if root is None:
                return None

            left = traverse(root.left)
            right = traverse(root.right)
            node = (root.val, left, right)

            if node in visited:
                visited[node][1] = True
                return visited[node][0]
            else:
                subtree_id = len(visited)
                visited[node] = [subtree_id, False, root]
                return subtree_id

        traverse(root)
        
        return [visit[2] for visit in visited.values() if visit[1] == True]
        