class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
    
        def dfs(left: int, right: int) -> int:

            if left > right:
                return 0

            pick_left = nums[left] - dfs(left + 1, right)
            pick_right = nums[right] - dfs(left, right - 1)
          
            return max(pick_left, pick_right)
      
        return dfs(0, len(nums) - 1) >= 0