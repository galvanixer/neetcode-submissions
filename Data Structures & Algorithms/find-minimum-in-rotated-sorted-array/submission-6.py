class Solution:

    # > Brute Force Solution. Time: O(n), Space: O(1)
    def findMin(self, nums:List[int]) -> int:
        return min(nums)
    
    # def findMin(self, nums: List[int]) -> int:

    #     n = len(nums)
    #     l, r = 0, n-1
    #     last = n - 1

    #     while l <= r:
    #         mid = (l+r)//2
    #         if nums[mid] <= nums[last]:
    #             r = mid - 1
    #         else:
    #             l = mid + 1

    #     return nums[l]

         