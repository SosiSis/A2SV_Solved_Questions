# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def calculate_max_gain(node: Optional[TreeNode]) -> int:

            if node is None:
                return 0
          
            left_gain = max(0, calculate_max_gain(node.left))
            right_gain = max(0, calculate_max_gain(node.right))
          
            current_max_path = node.val + left_gain + right_gain
          
            nonlocal max_sum
            max_sum = max(max_sum, current_max_path)
    
            return node.val + max(left_gain, right_gain)
      
        max_sum = float('-inf')
      
        calculate_max_gain(root)
      
        return max_sum