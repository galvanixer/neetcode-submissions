class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 1. Brute Force
        # maxlen = 0
        # for l in range(len(s)):
        #     countdict = {}
        #     maxf = 0
        #     for r in range(l, len(s)):
        #         countdict[s[r]] = countdict.get(s[r],0) + 1
        #         maxf = max(maxf, countdict[s[r]])
        #         # maxf = max(maxf, max(countdict.values()))
        #         if ((r-l+1)-maxf)<=k:
        #             maxlen = max(maxlen, r-l+1)

        # return maxlen

        # 2. Sliding Window
        maxlen = 0
        l = 0
        maxf = 0
        countdict = {}
        for r in range(len(s)):
            countdict[s[r]] = 1 + countdict.get(s[r], 0)
            maxf = max(maxf, countdict[s[r]])

            while ((r-l+1)-maxf)>k: # While invalid
                countdict[s[l]]-=1
                l += 1

            maxlen = max(maxlen, r-l+1)

        return maxlen


