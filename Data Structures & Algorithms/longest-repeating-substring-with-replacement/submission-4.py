class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxlength = 0
        left = 0
        seen = [0]*26

        # Add first, then repair
        for (right, char) in enumerate(s):
            seen[ord(char)-ord("A")] += 1
            diff = sum(seen) - max(seen)

            # Repair while invalid
            while (sum(seen) - max(seen)) > k:
                seen[ord(s[left])-ord("A")] -= 1
                left += 1

            maxlength = max(maxlength, sum(seen))

        return maxlength

            


        