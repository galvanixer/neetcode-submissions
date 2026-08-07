class Solution:

    # > Brute Force Solution. Time: O(n), Space: O(1)
    def findMin(self, nums:List[int]) -> int:
        return min(nums)
    
    # > Optimal Solution: 
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        nlast = nums[n-1]

        while l < r:
            mid = l + (r-l)//2
            if nums[mid] <= nlast: # = here is to include the last element.
                r = mid
            else:
                l = mid + 1
            
        return nums[l]

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        nlast = nums[n-1]

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] <= nlast: # = here is to include the last element.
                r = mid - 1
            else:
                l = mid + 1
            
        return nums[l]

         