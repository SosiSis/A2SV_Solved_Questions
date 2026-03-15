class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        res=0
        for bracket in s:
            if stack and bracket == ')':
                stack.pop()
                res+=1
            else:
                stack.append(bracket)
        return res