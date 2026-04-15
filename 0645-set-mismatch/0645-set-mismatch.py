class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set = set()
        duplicate = -1
        n = len(nums)
        
        actual_sum = 0
        for num in nums:
            if num in num_set:
                duplicate = num  # Found the duplicate
            num_set.add(num)
            actual_sum += num
        
        expected_sum = n * (n + 1) // 2
        missing = expected_sum - (actual_sum - duplicate)  # Correct sum by removing duplicate
        
        return [duplicate, missing]