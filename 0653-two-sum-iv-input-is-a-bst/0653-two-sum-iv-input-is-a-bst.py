# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
      
        def dfs(node: Optional[TreeNode]) -> bool:
        
            if node is None:
                return False
          
            complement = k - node.val
            if complement in visited_values:
                return True
          
            visited_values.add(node.val)
          
            return dfs(node.left) or dfs(node.right)
      
        visited_values = set()
      
        return dfs(root)
