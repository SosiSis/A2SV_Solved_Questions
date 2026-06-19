class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = acc = 0

        for it in gain:
            acc += it
            d = acc - ans
            ans += d & ~(d >> 0x1F)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna