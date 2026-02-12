class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        current_even_sum = sum(x for x in nums if x % 2 == 0)
        result = []
        
        for val, idx in queries:
            old_val = nums[idx]
            
            if old_val % 2 == 0:
                current_even_sum -= old_val
            
            nums[idx] += val
            new_val = nums[idx]
            
            if new_val % 2 == 0:
                current_even_sum += new_val
                
            result.append(current_even_sum)
            
        return result