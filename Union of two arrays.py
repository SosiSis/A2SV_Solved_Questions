class Solution:    
    def findUnion(self, a, b):
        # code here
        ans=sorted(list(set(a)|set(b)))
        return ans