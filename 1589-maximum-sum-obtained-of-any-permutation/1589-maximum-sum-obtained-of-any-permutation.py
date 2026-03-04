class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
      
        frequency = [0] * n
     
        for left, right in requests:
            frequency[left] += 1
            if right + 1 < n:
                frequency[right + 1] -= 1
      
        for i in range(1, n):
            frequency[i] += frequency[i - 1]
      

        nums.sort()
        frequency.sort()
  
        MOD = 10**9 + 7
        max_sum = sum(num * freq for num, freq in zip(nums, frequency)) % MOD
      
        return max_sum
