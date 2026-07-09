class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictanagrams = defaultdict(list)
        base = ord("a")
        for s in strs:
            charcounts = [0] * 26
            for character in s:
                ind = ord(character) - base
                charcounts[ind] += 1

            dictanagrams[tuple(charcounts)].append(s)
            
        return list(dictanagrams.values())

        