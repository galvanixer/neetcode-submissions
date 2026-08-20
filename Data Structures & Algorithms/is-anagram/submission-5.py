class Solution:
    # > Optimal Hash Map Solution. Time: O(n), Space: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        charcount = defaultdict(int)

        for char in s:
            charcount[char] += 1

        for char in t:
            charcount[char] -= 1

        if any(charcount.values()):
            return False

        return True

    # > Optimcal 
        