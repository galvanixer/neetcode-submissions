class Solution:

    # > Brute Force Solution. Time: O(nmlogm), Space: O(m)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        s1_sorted = sorted(s1) # Time: O(m logm) where m is number of characters in s1, Space: O(m)
        if n < m:
            return False

        # A total of ~n loops. Hence, Time: O(nmlogm)
        for idx in range(n-m+1):
            ss_s2_sorted = sorted(s2[idx:idx+m]) # Time: O(mlogm), Space: O(m)
            if ss_s2_sorted == s1_sorted:
                return True


        return False

        