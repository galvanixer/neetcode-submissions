class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{" 
        }
        lenstring = len(s)
        if lenstring % 2 == 1:
            return False
        
        for c in s:
            if c in "([{":
                stack.append(c)
            elif len(stack)!=0 and stack[-1]== pairs[c]:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False



