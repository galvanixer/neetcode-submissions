class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxlength = 0
        left = 0
        seen = [0]*26
        maxcount = 0

        # Add first, then repair
        for (right, char) in enumerate(s):
            seen[ord(char)-ord("A")] += 1
            maxcount = max(maxcount, seen[ord(char)-ord("A")])

            # Repair while invalid
            while (right-left+1 - maxcount) > k:
                seen[ord(s[left])-ord("A")] -= 1
                left += 1

            maxlength = max(maxlength, right-left+1)

        return maxlength

            


        