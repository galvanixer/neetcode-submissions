class Solution:

    # 1. Brute Force
    def isPalindrome(sefl, s:str) -> bool:
        sforward = "".join(char.lower() if char.isalnum() else "" for char in s)
        sreverse = "".join(char.lower() if char.isalnum() else "" for char in s[::-1])
        
        return sforward == sreverse


    # def isPalindrome(self, s: str) -> bool:
    
    #     ispalindrome = True
    #     left, right = 0, (len(s)-1)
    #     while left<right:
    #         while left<right and not(s[left].isalnum()):
    #             left += 1

    #         while right>left and not(s[right].isalnum()):
    #             right -= 1

    #         ispalindrome = (s[left].lower() == s[right].lower())
    #         if not(ispalindrome):
    #             return False

    #         left += 1
    #         right -= 1

    #     return ispalindrome


        