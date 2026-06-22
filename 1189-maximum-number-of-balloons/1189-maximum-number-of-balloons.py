class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_dict = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        
        text_dict = defaultdict(int)

        for char in text:
            if char in balloon_dict:
                text_dict[char] += 1

        res = float('inf')

        for char, freq in balloon_dict.items():
            res = min(res, text_dict[char] // freq)

        return 0 if res == float('inf') else res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna