class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        num_even_indices = (n + 1) // 2  
        num_odd_indices = n // 2     
        
        result = (pow(5, num_even_indices, MOD) * pow(4, num_odd_indices, MOD)) % MOD
        
        return result
     