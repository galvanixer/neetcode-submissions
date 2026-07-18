class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # 1. Brute Force
        # n = len(nums)
        # out = [1]*n

        # for i in range(n):
        #     for j in range(n):
        #         if j!=i :
        #             out[i] *= nums[j]

        # return out

        # 2. We can try to avoid the repeated work by storing the product of all non-zero numbers first.
        n = len(nums)
        out = [0]*n
        prodnonzero = 1
        zeroidxs = []

        for (i,n) in enumerate(nums):
            if n != 0:
                prodnonzero *= n
            else:
                zeroidxs.append(i)

        if len(zeroidxs)==1:
            out[zeroidxs[0]] = prodnonzero
        elif len(zeroidxs)==0:
            for (i,n) in enumerate(nums):
                out[i] = int(prodnonzero/n)

        return out



