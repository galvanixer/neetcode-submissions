class Solution:

    # Optimal Solution using two pointer strategy: Time: O(), Space: O()
    def isPalindrome(self, s:str) -> bool:
        n = len(s)
        left, right = 0, n-1

        while left < right: 
            
            while (left < right) and not s[left].isalnum():
                left += 1

            while (left < right) and not s[right].isalnum():
                right -=1
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


    # 1. Brute Force
    # def isPalindrome(sefl, s:str) -> bool:
    #     sforward = "".join(char.lower() if char.isalnum() else "" for char in s)

    #     return sforward == sforward[::-1]


    # def isPalindrome(self, s: str) -> bool:
    
    #     left, right = 0, (len(s)-1)
    #     while left<right:
    #         while left<right and not(s[left].isalnum()):
    #             left += 1

    #         while right>left and not(s[right].isalnum()):
    #             right -= 1

    #         if s[left].lower() != s[right].lower():
    #             return False

    #         left += 1
    #         right -= 1

    #     return True


        