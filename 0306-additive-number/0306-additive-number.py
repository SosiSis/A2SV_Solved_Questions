
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def isValid(x: str) -> bool:
            return len(x) == 1 or x[0] != '0'

        def backtrack(first: int, second: int, start: int) -> bool:
            if start == n:
                return True 
            
            third = first + second
            third_str = str(third)
            third_len = len(third_str)
            
            if num[start:start+third_len] != third_str:
                return False
            
           
            return backtrack(second, third, start + third_len)

        
        for i in range(1, n):
            for j in range(i+1, n):
                num1 = num[:i]
                num2 = num[i:j]
                if not isValid(num1) or not isValid(num2):
                    continue

                first, second = int(num1), int(num2)

                if backtrack(first, second, j):
                    return True

        return False



        