class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
       
        def dfs(index: int, last_value: int, current_path: List[int]) -> None:
      
            if index == len(nums):
            
                if len(current_path) > 1:
                    result.append(current_path[:])  
                return
          
            if nums[index] >= last_value:
                current_path.append(nums[index])
                dfs(index + 1, nums[index], current_path)
                current_path.pop()  

            if nums[index] != last_value:
                dfs(index + 1, last_value, current_path)
      
        result = []

        dfs(0, -1000, [])
      
        return result