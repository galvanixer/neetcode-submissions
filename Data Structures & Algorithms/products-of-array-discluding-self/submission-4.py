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

        # # 2. We can try to avoid the repeated work by storing the product of all non-zero numbers first.
        # n = len(nums)
        # out = [0]*n
        # prodnonzero = 1
        # zeroidxs = []

        # for (i,num) in enumerate(nums):
        #     if num:
        #         prodnonzero *= num
        #     else:
        #         zeroidxs.append(i)

        # if len(zeroidxs)==1:
        #     out[zeroidxs[0]] = prodnonzero
        # elif len(zeroidxs)==0:
        #     for (i,num) in enumerate(nums):
        #         out[i] = prodnonzero // num

        # return out

        # 3. Let's try prefix and suffix kind of solution.
        n = len(nums)
        out = [1]*n

        # Prefix
        prefixprod = 1
        for (idx,num) in enumerate(nums):
            out[idx] *= prefixprod
            prefixprod *= num

        suffixprod = 1
        for idx in range(n-1, -1, -1):
            num = nums[idx]
            out[idx] *= suffixprod
            suffixprod *= num

        return out

        



