from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, used):
            # If the permutation is done
            if len(path) == len(nums):
                result.append(path[:])
                return
            # Go through all numbers in `nums`
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Mark the number as used
                used[i] = True
                # Add the number to the current path
                path.append(nums[i])
                # Continue building the permutation
                backtrack(path, used)
                # Backtrack, remove the number from the path and mark it as unused
                path.pop()
                used[i] = False

        result = []
        used = [False] * len(nums)
        backtrack([], used)
        return result
