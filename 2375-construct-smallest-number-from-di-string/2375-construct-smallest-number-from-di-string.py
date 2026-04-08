class Solution:
    def smallestNumber(self, pattern: str) -> str:      
        def backtrack(position: int) -> None:
        
            nonlocal result
          
            if result:
                return

            if position == len(pattern) + 1:
                result = ''.join(current_number)
                return

            for digit in range(1, 10):
                
                if used_digits[digit]:
                    continue

                if position > 0:
                    last_digit = int(current_number[-1])
                  
                    if pattern[position - 1] == 'I' and last_digit >= digit:
                        continue
                  
                    if pattern[position - 1] == 'D' and last_digit <= digit:
                        continue

                used_digits[digit] = True
                current_number.append(str(digit))
              
                backtrack(position + 1)
              
                current_number.pop()
                used_digits[digit] = False
      
        used_digits = [False] * 10  
        current_number = []  
        result = None  
      
        backtrack(0)
      
        return result