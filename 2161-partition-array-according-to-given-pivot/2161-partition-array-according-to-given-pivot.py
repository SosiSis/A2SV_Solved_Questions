class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
       less, equal ,greater= [],[],[]
       for i in range(len(nums)):
            if nums[i]<pivot:
                less.append(nums[i])
            elif  nums[i]>pivot:
                greater.append(nums[i])
            else:
                equal.append(nums[i]) 
       return less + equal + greater

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna