from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
      
        prefix_diff = [0] * (len(s) + 1)

        for left, right, d in shifts:
           
            if d == 1:
              prefix_diff[left] += 1   
              prefix_diff[right + 1] -= 1
              
            else:
                prefix_diff[left] -= 1   
                prefix_diff[right + 1] += 1

        current = 0
        shifted = []

        for idx,char in enumerate(s):
            current += prefix_diff[idx]
            val = ord(char) - ord("a")
            new_val = (current + val) % 26
            shifted.append(chr(new_val + ord("a")))
            
        return "".join(shifted)
