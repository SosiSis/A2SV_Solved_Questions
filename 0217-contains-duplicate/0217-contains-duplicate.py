class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newDic=Counter(nums)
        for key,value in newDic.items():
            if value >= 2 :
                return True
                
        return False