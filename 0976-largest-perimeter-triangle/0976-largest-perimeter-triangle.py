from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        res=0
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if b + c > a:
                perimeter=a + b + c
                res = max(res,perimeter)
        return res
