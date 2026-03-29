# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:      
        def dfs(node: TreeNode, parent_val: int) -> int:

            if node is None:
                return 0
          
            total_sum = dfs(node.left, node.val) + dfs(node.right, node.val)
          
            if parent_val % 2 == 0:

                if node.left:
                    total_sum += node.left.val
            
                if node.right:
                    total_sum += node.right.val
          
            return total_sum
      
        return dfs(root, 1)
