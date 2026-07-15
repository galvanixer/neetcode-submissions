class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqcount = defaultdict(int)
        if len(s) != len(t):
            return False

        for c in s:
            freqcount[c]+=1

        for c in t:
            if c in freqcount.keys():
                freqcount[c]-=1

        if any(v!=0 for v in freqcount.values()):
            return False

        return True


        