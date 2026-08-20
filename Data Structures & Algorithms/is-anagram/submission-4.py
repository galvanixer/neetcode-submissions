class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charcount = defaultdict(int)

        for char in s:
            charcount[char] += 1

        for char in t:
            charcount[char] -= 1

        if any(charcount.values())!=0:
            return False

        return True
        