class Solution:
    def isValid(self, s: str) -> bool:
        pairs={
            '}' : '{' ,
            ']' : '[',
            ')' :'('
            }

        stack=[]
        for symbol in s:
            if symbol in pairs.values() :
                stack.append(symbol)
            else:
                if  not stack: return False
                elif pairs[symbol] != stack[-1]: return False
                else: stack.pop()

        return True if not stack else False            