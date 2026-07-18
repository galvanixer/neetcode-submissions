class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Brute Force Solution.
        res = 0
        setnums = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in setnums:
                streak += 1
                curr += 1

            res = max(res, streak)

        return res



        # 2. Solution using Sorting.
        # sortednums = sorted(set(x))
        
        # # 3. Use of Hash Set
        # setnums = set(nums)
        # longest = 0
        # for num in setnums:
        #     if (num-1) not in setnums:
        #         length = 1
        #         while (num+length) in setnums:
        #             length += 1

        #         longest = max(longest, length)

        # return longest

        # 4. Use of Hash Map




