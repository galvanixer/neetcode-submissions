class Solution:
    # We are trying to use dictionary here which is O(1) in access but is costlier
    # than directly accessing an array.
    # def isAnagram(self, s: str, t: str) -> bool:
    #     freqcount = defaultdict(int)
    #     if len(s) != len(t):
    #         return False

    #     for c in s:
    #         freqcount[c]+=1

    #     for c in t:
    #         if c in freqcount.keys():
    #             freqcount[c]-=1

    #     if any(v!=0 for v in freqcount.values()):
    #         return False

    #     return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqcount = [0]*26
        baseord = ord("a")
        for c in s:
            freqcount[ord(c) - baseord] += 1

        for c in t:
            freqcount[ord(c) - baseord] -= 1

        if any(v!=0 for v in freqcount):
            return False

        return True


        