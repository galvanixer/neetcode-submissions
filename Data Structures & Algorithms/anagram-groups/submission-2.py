class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        baseord = ord("a")
        resdict = defaultdict(list)
        res = []
        for s in strs:
            freqcount = [0]*26
            for char in s:
                freqcount[ord(char)-baseord]+=1
            resdict[tuple(freqcount)].append(s)

        for v in resdict.values():
            res.append(v)

        return res



        