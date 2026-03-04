class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1}
        total=0

        for idx,value in enumerate(nums):
            total += value
            r=total % k
            if r not in remainder:
                remainder[r]=idx

            elif (idx - remainder[r] )  > 1:
                return True

        return False