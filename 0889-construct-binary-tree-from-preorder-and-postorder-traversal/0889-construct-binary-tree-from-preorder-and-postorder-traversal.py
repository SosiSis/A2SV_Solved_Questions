# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
      
        def build_tree(
            pre_start: int, 
            pre_end: int, 
            post_start: int, 
            post_end: int
        ) -> Optional[TreeNode]:
     

            if pre_start > pre_end:
                return None

            root = TreeNode(preorder[pre_start])
          
            if pre_start == pre_end:
                return root
          
            left_root_val = preorder[pre_start + 1]
            left_root_post_idx = postorder_index_map[left_root_val]
          
            left_subtree_size = left_root_post_idx - post_start + 1
          
            root.left = build_tree(
                pre_start + 1,                          
                pre_start + left_subtree_size,          
                post_start,                             
                left_root_post_idx                    
            )
          
            root.right = build_tree(
                pre_start + left_subtree_size + 1,      
                pre_end,                               
                left_root_post_idx + 1,                
                post_end - 1                          
            )
          
            return root
      
        postorder_index_map = {val: idx for idx, val in enumerate(postorder)}

        return build_tree(0, len(preorder) - 1, 0, len(postorder) - 1)
