class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Brute Force Solution.


        # 3. Use of Hash Set
        setnums = set(nums)
        longest = 0
        for num in setnums:
            if (num-1) not in setnums:
                numtosearch = num
                streak = 0
                while numtosearch in setnums:
                    streak += 1
                    numtosearch += 1

                longest = max(longest, streak)

        return longest




