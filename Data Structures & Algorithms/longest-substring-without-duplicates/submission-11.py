class Solution:

    # > STYLE 1: Check and repair first, then add
    # > Sliding Window Solution. Time: O(n), Space: O(m) where m is unique characters in the string
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxlength = 0
        seen = set()
        n = len(s)

        left = 0
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            maxlength = max(maxlength, len(seen))

        return maxlength

    # > STYLE 2: Add first, then repair.
    # > Sliding Window Solution. Time: O(n), Space: O(m) where m is unique characters in the string
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxlength = 0
        seen = defaultdict(int)
        n = len(s)
        left = 0

        for right in range(n):
            seen[s[right]] += 1
            while seen[s[right]]>1:
                seen[s[left]] -= 1
                left += 1
            
            maxlength = max(maxlength, right-left+1)

        return maxlength
