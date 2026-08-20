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

    # > Optimal Hash Table Solution. Time: O(n), Space: O(1)
    def isAnagram(self, s:str, t:str) -> bool:
        charcount = [0]*26

        for char in s:
            charcount[ord(char) - ord("a")] += 1

        for char in t:
            charcount[ord(char) - ord("a")] -= 1

        return not any(charcount)
        