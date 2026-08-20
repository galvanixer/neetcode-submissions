class Solution:
    # > Optimal Solution. Time: O(), Space: O()
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramdict = {}
        # Time: O(m*n), Space: O(m)
        for s in strs:
            charcount = [0]*26
            for char in s:
                charcount[ord(char) - ord("a")] += 1

            if tuple(charcount) in anagramdict:
                anagramdict[tuple(charcount)].append(s)
            else:
                anagramdict[tuple(charcount)]=[s]

        res = []
        for v in anagramdict.values():
            res.append(v)

        return res

        