class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res=[]
        dic_list1={val:idx for idx,val in enumerate(list1)}
        sum=float('inf')
        for idx,val in enumerate(list2):
            
            if val in dic_list1:
                cur_sum=idx + dic_list1[val]

                if cur_sum<sum:
                    sum=cur_sum
                    res=[val]
                elif cur_sum== sum:
                    res.append(val)

        return res
        