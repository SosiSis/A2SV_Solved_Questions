class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0
        
        for i in range(n):
            sumOdd += (2 * i + 1)  
        
        for j in range(1,n):
            sumEven += (2 * (j ))  
        
        return math.gcd(sumOdd, sumEven)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna