class Solution:
    # > Optimal Solution: time: O(logn), space: O(1)
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        searchidx = -1

        while left<=right:
            mid = left + (right-left)//2 # So that in languages like C it does not overflow.
            if nums[mid] == target:
                searchidx = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return searchidx
        