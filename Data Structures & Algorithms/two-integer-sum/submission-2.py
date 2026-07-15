class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        residualdict = {}
        for (i,n) in enumerate(nums):
            residual = target - n
            if residual in residualdict:
                return [residualdict[residual], i]
            else:
                residualdict[n] = i


                