class Solution:
    def distributeCookies(self,cookies, k):
        res = [float('inf')]  
        children = [0] * k    

        def backtrack(i):
            if i == len(cookies):  
                res[0] = min(res[0], max(children))  
                return

            for j in range(k):
                children[j] += cookies[i]      
                backtrack(i + 1)              
                children[j] -= cookies[i]     

                
                if children[j] == 0:
                    break

        backtrack(0)
        return res[0]
 