# The brute force way which I can think of is c
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqcount = {} # Declaring dictionary to store frequency count.
        for character in s:
            freqcount[character] = freqcount.get(character, 0) + 1

        for character in t:
            freqcount[character] = freqcount.get(character, 0) - 1

        return all(value == 0 for value in freqcount.values())

        