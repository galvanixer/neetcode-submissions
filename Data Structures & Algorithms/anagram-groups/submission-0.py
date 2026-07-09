class Solution:
    def characterCountTuple(self, inputstr: str) -> Tuple[int]:
        base = ord("a") # to be used for index estimation later.
        charcounts = [0]*26
        for character in inputstr:
            index_character = ord(character) - base
            charcounts[index_character] += 1
        
        return tuple(charcounts)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictanagrams: Dict[Tuple[int], List[str]] = {}

        for s in strs:
            charcounts = self.characterCountTuple(s)
            if charcounts in dictanagrams:
                dictanagrams[charcounts].append(s)
            else:
                dictanagrams[charcounts] = [s]
            
        return list(dictanagrams.values())

        