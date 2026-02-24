class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()
        n = len(piles) // 3
        total_coins = 0
        curr = len(piles) - 2
        
        for _ in range(n):
            total_coins += piles[curr]
            curr -= 2  
            
        return total_coins