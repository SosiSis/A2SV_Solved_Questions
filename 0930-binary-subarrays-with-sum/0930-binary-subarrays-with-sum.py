class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            if x < 0:
                return 0

            res=0
            left=0
            cur=0

            for right in range(len(nums)):
                cur += nums[right]

                while cur > x:
                    cur -= nums[left]
                    left += 1
                res += (right - left + 1)

            return res

        return helper(goal) - helper(goal - 1)    