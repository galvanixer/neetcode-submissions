class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicttarget: dict[int,int] = {}
        for i in range(len(nums)):
            num = nums[i]
            diffnum = target - num
            if diffnum in dicttarget:
                j = dicttarget[diffnum]
                out = [j, i]
                return out
            
            dicttarget[num] = i


                