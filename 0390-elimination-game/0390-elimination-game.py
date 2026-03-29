class Solution:
    def lastRemaining(self, n: int) -> int:
        
        first_element = 1
        last_element = n
      
        iteration = 0
        step_size = 1
        remaining_count = n
      
        while remaining_count > 1:
            if iteration % 2 == 1:
                
                last_element -= step_size
              
                if remaining_count % 2 == 1:
                    first_element += step_size
            else:
                first_element += step_size
              
                if remaining_count % 2 == 1:
                    last_element -= step_size
        
            remaining_count //= 2
            step_size *= 2
            iteration += 1
      
        return first_element
