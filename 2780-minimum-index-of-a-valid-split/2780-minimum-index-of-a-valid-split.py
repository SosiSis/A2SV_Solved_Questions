class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
    
        counts = Counter(nums)
        dominant_element = -1
        total_count = 0
        
        for val, freq in counts.items():
            if freq * 2 > n:
                dominant_element = val
                total_count = freq
                break
                
        count_left = 0
        for i in range(n - 1):
            if nums[i] == dominant_element:
                count_left += 1
            
            len_left = i + 1
            len_right = n - len_left
            
            count_right = total_count - count_left
            
            if count_left * 2 > len_left and count_right * 2 > len_right:
                return i
                
        return -1
            