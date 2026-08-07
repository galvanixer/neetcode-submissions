class Solution:

    # > Brute Force Solution. Time: O(n), Space: O(1)
    def findMin(self, nums:List[int]) -> int:
        return min(nums)
    
    # > Binary Search Solution. Time: O(logn), Space: O(1)
    def findMin(self, nums:List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1

        # Predicate P(i) = nums[i] <= nums[n-1]
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid + 1

        return nums[right]

         