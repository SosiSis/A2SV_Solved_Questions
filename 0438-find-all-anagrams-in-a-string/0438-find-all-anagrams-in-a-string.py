class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s)<len(p):
            return []
        window=Counter(p)
        left=0
        res=[]
        
        cur_window=Counter()
        for i in range(len(p)):
            cur_window[s[i]] += 1
        
        if window == cur_window:
            res.append(0)

        for right in range(len(p),len(s)):
            cur_window[s[right]] += 1
            cur_window[s[left]] -= 1

            left+=1

            if window == cur_window:
                res.append(left)
            
            

        return res