class Solution:

    # > Brute Force Solution: Time: O(n^2), Space: O(1)
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxlength = 0 # Maximum length of longest repeating character after k replacement
        for (idx, c) in enumerate(s):
            maxcount = 0 # Maximum length after replacement for substring starting at index idx
            diff = 0 # No. of different elements than c
            for j in range(idx,n):
                if s[j] != c:
                    diff += 1
                if diff > k:
                    break
                maxcount += 1

            maxlength = max(maxlength, maxcount)

        return maxlength




    # > Optimal Solution: Time: O(n), Space: O(1)
    def characterReplacement(self, s: str, k: int) -> int:

        maxlength = 0
        left = 0
        seen = [0]*26
        maxcount = 0

        # Add first, then repair
        for (right, char) in enumerate(s):
            idx = ord(char)-ord("A")
            seen[idx] += 1
            maxcount = max(maxcount, seen[idx])

            # Repair while invalid
            while (right-left+1 - maxcount) > k:
                seen[ord(s[left])-ord("A")] -= 1
                left += 1

            maxlength = max(maxlength, right-left+1)

        return maxlength

            


        