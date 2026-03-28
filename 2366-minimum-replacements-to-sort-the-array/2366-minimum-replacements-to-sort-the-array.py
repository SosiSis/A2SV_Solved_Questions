class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
 
        total_operations = 0
        array_length = len(nums)

        max_allowed_value = nums[-1]
 
        for index in range(array_length - 2, -1, -1):
            current_value = nums[index]
          
            if current_value <= max_allowed_value:
                max_allowed_value = current_value
                continue

            num_parts = (current_value + max_allowed_value - 1) // max_allowed_value

            total_operations += num_parts - 1
          
            max_allowed_value = current_value // num_parts
      
        return total_operations