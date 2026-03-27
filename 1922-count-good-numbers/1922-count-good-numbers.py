class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Calculate number of even index digits and odd index digits
        num_even_indices = (n + 1) // 2  # Ceiling of n/2
        num_odd_indices = n // 2         # Floor of n/2
        
        # Calculate the result using modular exponentiation
        result = (pow(5, num_even_indices, MOD) * pow(4, num_odd_indices, MOD)) % MOD
        
        return result
     