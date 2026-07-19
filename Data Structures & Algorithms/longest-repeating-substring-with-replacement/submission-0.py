class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 1. Brute Force
        maxlen = 0
        for l in range(len(s)):
            countdict = {}
            maxf = 0
            for r in range(l, len(s)):
                countdict[s[r]] = countdict.get(s[r],0) + 1
                maxf = max(maxf, countdict[s[r]])
                if ((r-l+1)-maxf)<=k:
                    maxlen = max(maxlen, r-l+1)

        return maxlen

