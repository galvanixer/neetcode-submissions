class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. My Brute Force Solution
        sforward = "".join(c.lower() for c in s if c.isalnum())
        srev = sforward[::-1]
        if sforward == srev:
            return True
        return False