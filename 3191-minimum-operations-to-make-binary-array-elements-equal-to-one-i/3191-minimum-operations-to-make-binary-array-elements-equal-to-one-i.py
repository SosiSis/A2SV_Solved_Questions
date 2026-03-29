class Solution:
    def minOperations(self, nums: List[int]) -> int:
      
        operation_count = 0
      
        for index, value in enumerate(nums):
            
            if value == 0:
                if index + 2 >= len(nums):
                    return -1

                nums[index + 1] ^= 1  
                nums[index + 2] ^= 1  
              
                operation_count += 1
      
        return operation_count