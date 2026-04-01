class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans=-1

        def possible(mid):
            hour = 0
            for p in piles:
                hour += math.ceil(p/mid)
            return hour <= h

        while left <= right:
            mid =left + (right - left) // 2
            if possible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans     
