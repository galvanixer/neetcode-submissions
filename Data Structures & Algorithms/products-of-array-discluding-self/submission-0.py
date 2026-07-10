class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # with division operation
        prod = 1
        zeroidxs = []
        for (i,x) in enumerate(nums):
            if x!=0: 
                prod *= x
            else:
                zeroidxs.append(i)

        nzeroidxs = len(zeroidxs)

        res = [0]*len(nums)
            
        if (nzeroidxs==1):
            res[zeroidxs[0]] = prod
        elif (nzeroidxs ==0):    
            for (i,num) in enumerate(nums):
                res[i]=(int(prod/num))

        return res