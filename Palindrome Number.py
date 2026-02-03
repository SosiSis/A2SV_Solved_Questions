class Solution:
    def isPalindrome(self, x: int) -> bool:
        isPal=str(x)
        n=len(isPal)
        l,r=0,n-1

        while l <= r:
            if isPal[l] == isPal[r]:
                l+=1
                r-=1
            else:
               return False
        return True        