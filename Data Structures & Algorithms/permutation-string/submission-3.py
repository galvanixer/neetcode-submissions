class Solution:

    # > Brute Force Solution. Time: O(nmlogm), Space: O(m)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2) # Length of bigger string s2
        m = len(s1) # Length of string s1

        s1_sorted = sorted(s1) # Time: O(mlogm)

        for i in range(n-m+1):
            if sorted(s2[i:i+m])==s1_sorted: # Time: O(mlogm)+O(m)~O(mlogm)
                return True

        return False


    # # > Optimal Solution.
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     n = len(s2)
    #     m = len(s1)
    #     if n < m:
    #         return False

    #     countdicts1 = defaultdict(int)
    #     for c in s1:
    #         countdicts1[c]+=1
        
    #     countdicts2 = defaultdict(int)
    #     left = 0
    #     for right in range(n):
    #         if right - left + 1 > m:
    #             countdicts2[s2[left]] -= 1
    #             left += 1

    #         if right - left + 1 == m:




