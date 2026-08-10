class Solution:

    # > Brute Force Solution
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ns2 = len(s2)
        ns1 = len(s1)
        s1_sorted = sorted(s1)
        if ns2 < ns1:
            return False

        for idx in range(ns2-ns1+1):
            ss_s2_sorted = sorted(s2[idx:idx+ns1])
            if ss_s2_sorted == s1_sorted:
                return True


        return False

        