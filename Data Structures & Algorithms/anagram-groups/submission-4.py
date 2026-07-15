class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        baseord = ord("a")
        resdict = defaultdict(list)

        for s in strs:
            freqcount = [0]*26
            for char in s:
                freqcount[ord(char)-baseord]+=1
            resdict[tuple(freqcount)].append(s)

        return list(resdict.values())



        