class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Brute Force Solution.


        # 3. Use of Hash Set
        setnums = set(nums)
        startingnums = []
        res = 0
        for num in setnums:
            if (num-1) in setnums:
                continue
            else:
                startingnums.append(num)

        for num in startingnums:
            numtosearch = num
            streak = 0
            while numtosearch in setnums:
                streak += 1
                numtosearch += 1

            res = max(res, streak)

        return res




