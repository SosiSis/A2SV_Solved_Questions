class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        placeholder_pointer=0
        seeker_pointer=0
        
        while seeker_pointer < len(nums):
            if nums[seeker_pointer] != 0:
                nums[seeker_pointer],nums[placeholder_pointer]= nums[placeholder_pointer] , nums[seeker_pointer]
                placeholder_pointer+=1
            seeker_pointer+=1

