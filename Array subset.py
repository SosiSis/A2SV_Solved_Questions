#User function Template for python3
from collections import Counter 
class Solution:
    #Function to check if b is a subset of a.
    def isSubset(self, a, b):
        
        count_a = Counter(a)
        count_b = Counter(b)
        for ele in count_b:
            if count_b[ele] > count_a[ele]:
                return False
        return True
    
    
    
    
