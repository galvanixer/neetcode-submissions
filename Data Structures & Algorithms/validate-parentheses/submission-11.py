class Solution:

    def isValid(self, s:str) -> bool:
        OPENING_BRACKETS = {"(","{","["}
        lenstring = len(s)
        stack = []
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }


        for (i, char) in enumerate(s):
            if char in OPENING_BRACKETS:
                stack.append(char)
            elif len(stack)>0 and stack[-1]==pairs[char]:
                stack.pop()
            else: 
                return False

        return (not stack)

            



































    # def isValid(self, s: str) -> bool:
    #     stack = []
    #     pairs = {
    #         ")" : "(",
    #         "]" : "[",
    #         "}" : "{" 
    #     }
    #     lenstring = len(s)
    #     if lenstring % 2 == 1:
    #         return False
        
    #     for c in s:
    #         if c in "([{":
    #             stack.append(c)
    #         elif stack and stack[-1]== pairs[c]:
    #             stack.pop()
    #         else:
    #             return False

    #     return len(stack) == 0



