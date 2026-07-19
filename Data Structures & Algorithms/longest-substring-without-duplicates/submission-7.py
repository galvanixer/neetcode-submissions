class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # 1. Brute Force
        # maxlen = 0
        # for (idx, char) in enumerate(s):
        #     char_set = set()
        #     for char in s[idx:] :
        #         if char in char_set:
        #             break
        #         char_set.add(char)
        #     maxlen = max(maxlen, len(char_set))

        # return maxlen

        # 2. Sliding Window
        left = 0
        char_set = set()
        maxlen = 0
        for right in range(len(s)):
            while s[right] in char_set: # while invalid
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            maxlen = max(maxlen, right-left+1)

        return maxlen





            
                

