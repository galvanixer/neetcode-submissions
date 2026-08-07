class Solution:
    # > Binary Search Solution: Time: O(logn)
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        # Boundary Binary Search: Time: O(logn)
        while left < right: 
            mid = left + (right - left)//2

            if nums[mid]<=nums[-1]:
                right = mid
            else:
                left = mid + 1

        # Minima index is given by this right and left
        minimaidx = right

        # Now we have to perform binary in one of the two sorted arrays.
        if target >= nums[minimaidx] and target <= nums[-1]:
            left, right = minimaidx, n-1
        else:
            left, right = 0, minimaidx-1

        # Exact Binary Search: Time: O(logn)
        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1

        return -1
        