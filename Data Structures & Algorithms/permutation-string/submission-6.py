class Solution:

    # > Brute Force Solution. Time: O(n.mlogm), Space: O(m)
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     n = len(s2) # Length of bigger string s2
    #     m = len(s1) # Length of string s1

    #     s1_sorted = sorted(s1) # Time: O(mlogm), Space: O(m)

    #     for i in range(n-m+1):
    #         if sorted(s2[i:i+m])==s1_sorted: # Time: O(mlogm)+O(m)~O(mlogm)
    #             return True

    #     return False


    # > Optimal Solution. Time: O(), Space: O()
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        if n<m:
            return False

        countdict_s1 = defaultdict(int)
        for char in s1:
            countdict_s1[char] += 1

        current_size = 0
        left = 0
        countdict_substring_s2 = defaultdict(int)
        for (right,char) in enumerate(s2):
            countdict_substring_s2[char] += 1

            if right-left+1 > m:
                countdict_substring_s2[s2[left]] -= 1
                left += 1
            
            if right-left+1 == m:
                matches = 0
                for key in countdict_s1.keys():
                    if countdict_substring_s2[key] == countdict_s1[key]:
                        matches += 1
                if matches == len(countdict_s1):
                    return True

        return False

            




    




