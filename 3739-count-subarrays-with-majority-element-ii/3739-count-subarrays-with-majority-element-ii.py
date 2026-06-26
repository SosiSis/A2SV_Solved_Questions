class Solution:
    def countMajoritySubarrays(self, nums: List[int], target_num: int) -> int:
    
        zero_balance_offset = len(nums) + 1
        curr_balance = zero_balance_offset
        
        balance_freqs = [0] * (zero_balance_offset * 2)
        balance_freqs[curr_balance] = 1
        
        subarr_cnt = 0
        cum_freq_sum = 0
        
        for num in nums:
        
            if num == target_num:
                cum_freq_sum += balance_freqs[curr_balance]
                curr_balance += 1
        
            else:
                curr_balance -= 1
                cum_freq_sum -= balance_freqs[curr_balance]

            balance_freqs[curr_balance] += 1
            subarr_cnt += cum_freq_sum
            
        return subarr_cnt

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna