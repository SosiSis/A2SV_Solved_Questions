# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def find_min(node):
            if not node:
                return 0
            
            if not node.left:
                return 1 + find_min(node.right)
            if not node.right:
                return 1 + find_min(node.left)
            
            return 1 + min(find_min(node.left), find_min(node.right))
        
        return find_min(root)