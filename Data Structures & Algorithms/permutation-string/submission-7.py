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


    # > Fixed Sliding Window Solution. Time: O(n*m), Space: O(m)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        if n<m:
            return False

        countdict_s1 = defaultdict(int)
        for char in s1:
            countdict_s1[char] += 1

        left = 0
        countdict_substring_s2 = defaultdict(int)
        for right, char in enumerate(s2):
            countdict_substring_s2[char] += 1

            # Keep window size <=m
            if right-left+1 > m:
                countdict_substring_s2[s2[left]] -= 1
                left += 1
            
            # Check every window of size m
            if right-left+1 == m:
                matches = 0
                for key in countdict_s1.keys():
                    if countdict_substring_s2[key] == countdict_s1[key]:
                        matches += 1
                if matches == len(countdict_s1):
                    return True

        return False

        # > Optimal Sliding Window Solution. Time: O(n), Space: O(1)
        def checkInclusion(self, s1: str, s2: str) -> bool:
            m, n = len(s1), len(s2)

            count_s1 = [0]*26
            count_s2 = [0]*26

            for i in range(m):
                count_s1[ord(s1[i])-ord("a")] += 1
                count_s2[ord(s2[i])-ord("a")] += 1

            # Number of character frequencies that currently match.
            matches = 0
            for i in range(26):
                if count_s1[i]==count_s2[i]:
                    matches += 1

            # Fixed size sliding window updates.
            left = 0
            for right in range(m, n):
                if matches == 26:
                    return True

                # Add new character entering the window.
                idx = ord(s2[right]) - ord("a")

                if count_s1[idx] == count_s2[idx]:
                    matches -= 1

                count_s2[idx] += 1
                if count_s1[idx] == count_s2[idx]:
                    matches += 1

                # Remove old character leaving the window
                idx = ord(s2[left]) - ord("a")

                if count_s1[idx] == count_s2[idx]:
                    matches -= 1

                count_s2[idx] -= 1
                if count_s1[idx] == count_s2[idx]:
                    matches += 1

                left += 1

            return matches == 26

            




    




