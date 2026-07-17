class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_num = max(nums)

        freq = [0] * (max_num + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (max_num + 1)
        for g in range(1, max_num + 1):
            for multiple in range(g, max_num + 1, g):
                cnt[g] += freq[multiple]

        exact = [0] * (max_num + 1)

        for g in range(max_num, 0, -1):
            c = cnt[g]
            exact[g] = c * (c - 1) // 2

            for multiple in range(2 * g, max_num + 1, g):
                exact[g] -= exact[multiple]

        prefix = []
        gcds = []
        total = 0

        for g in range(1, max_num + 1):
            if exact[g]:
                total += exact[g]
                prefix.append(total)
                gcds.append(g)

        ans = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            ans.append(gcds[idx])

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna