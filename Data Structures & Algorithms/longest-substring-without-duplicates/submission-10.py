class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # > Sliding Window Solution. Time: O(n), Space: O()
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