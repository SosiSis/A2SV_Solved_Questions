class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        a=sorted(a)
        b=sorted(b)
        return a == b