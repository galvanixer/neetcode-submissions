class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. Brute Force
        maxlen = 0
        for (idx, char) in enumerate(s):
            char_set = set()
            for char in s[idx:] :
                if char in char_set:
                    break
                char_set.add(char)
            maxlen = max(maxlen, len(char_set))
        print(len(set(s)))

        return maxlen



            
                

