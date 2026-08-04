class Solution:

    # > Burte Foce Solution. Time: 
    def isValid(self, s:str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")

        return s==""


    # 1. Optimal Solution. Time: O(n), Space: O(n)
    # def isValid(self, s:str) -> bool:
    #     OPENING_BRACKETS = {"(","{","["}
    #     lenstring = len(s)
    #     stack = []
    #     pairs = {
    #         ")" : "(",
    #         "]" : "[",
    #         "}" : "{"
    #     }

    #     if lenstring%2==1:
    #         return False

    #     for char in s:
    #         if char in OPENING_BRACKETS:
    #             stack.append(char)
    #         elif len(stack)>0 and stack[-1]==pairs[char]:
    #             stack.pop()
    #         else: 
    #             return False

    #     return (not stack)

          



































    



