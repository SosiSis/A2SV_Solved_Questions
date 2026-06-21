class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        xMin = xMax = max(costs)
        freq = [0] * (xMax + 1)
        for x in costs:
            freq[x] += 1
            xMin = min(xMin, x)
        cnt = 0
        for x, f in enumerate(freq[xMin:], start=xMin):
            if f == 0:
                continue
            buy = min(coins // x, f)
            if buy == 0:
                break
            cnt += buy
            coins -= buy * x
        return cnt

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna