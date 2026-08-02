class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        residual = {}
        out = []
        for (i,n) in enumerate(nums):
            diff = target - n
            if diff in residual:
                return [residual[diff], i]
            else:
                residual[nums[i]]=i