class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        residual = {}
        out = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in residual:
                out = [residual[diff], i]
            else:
                residual[nums[i]]=i

        return out