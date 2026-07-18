class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. Brute Force
        n = len(nums)
        out = [1]*n

        for i in range(n):
            for j in range(n):
                if j!=i :
                    out[i] *= nums[j]

        return out


        # out = [1]*len(nums)
        # outdict = defaultdict(int)

        # for (i,n) in enumerate(nums):

