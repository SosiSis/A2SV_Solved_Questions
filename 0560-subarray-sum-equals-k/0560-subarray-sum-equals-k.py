class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Counts the number of contiguous subarrays in 'nums' whose elements sum up to 'k'.

        Args:
            nums (List[int]): A list of integers.
            k (int): The target sum.

        Returns:
            int: The number of contiguous subarrays that sum to 'k'.
        """
        res=0
        curSum=0
        prefixSums={0:1}

        for n in nums:
            curSum += n
            diff =curSum -k

            res+= prefixSums.get(diff,0)
            prefixSums[curSum] =1 + prefixSums.get(curSum,0)

        return res 