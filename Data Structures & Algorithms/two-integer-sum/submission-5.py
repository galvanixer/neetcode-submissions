class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        residual_dict = defaultdict(int)

        for (idx,n) in enumerate(nums):
            residual = target - n
            if residual in residual_dict:
                return [residual_dict[residual], idx]
            residual_dict[n] = idx

        return []