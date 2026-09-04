class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        res=[]
        n=len(nums)
        

        for i in range(n):
            largest=nums[:i+1]
            smallest=nums[i:]
            if ( max(largest)- min(smallest) ) <= k:
                res.append(i)
        return min(res) if res else -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna