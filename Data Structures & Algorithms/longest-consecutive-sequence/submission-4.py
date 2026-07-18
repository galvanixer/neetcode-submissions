class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Brute Force Solution.

        # 2. Solution using Sorting.

        # 3. Use of Hash Set
        setnums = set(nums)
        longest = 0
        for num in setnums:
            if (num-1) not in setnums:
                length = 1
                while (num+length) in setnums:
                    length += 1

                longest = max(longest, length)

        return longest

        # 4. Use of Hash Map




