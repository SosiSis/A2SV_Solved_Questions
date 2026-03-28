class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
    
        max_reachable = 1

        patches_count = 0
      
        index = 0

        while max_reachable <= n:
        
            if index < len(nums) and nums[index] <= max_reachable:
             
                max_reachable += nums[index]
                index += 1
            else:

                patches_count += 1
                max_reachable *= 2  
      
        return patches_count
