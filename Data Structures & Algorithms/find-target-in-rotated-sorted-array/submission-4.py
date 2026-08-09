class Solution:

    # > Two Pass Binary Search: Time: O(logn)
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        # Since the array is divided into two sorted subarrays.
        # The second array starts at the minima. So if we can find
        # the minima, we will have two sorted arrays and we can perform
        # binary search on them.
        # 1. First doing the boundary search to find the minima.
        while left < right: # Since mid is included in the search.
            mid = left + (right-left)//2
            if nums[mid] <= nums[-1]: # predicate
                right = mid
            else:
                left = mid + 1

        pivot = left # This is the idx corresponding to the minima.
        print("Pivot: ", pivot)

        # Now we will perform the exact search to find the target.
        if target <= nums[-1]:
            left, right = pivot, n-1
        else:
            left, right = 0, pivot - 1

        while left <= right:
            mid = left + (right - left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid - 1
            else:
                left = mid + 1

        return -1



    # # > Brute Force Solution: Time: O(n)
    # def search(self, nums: List[int], target: int) -> int:
    #     for (idx, n) in enumerate(nums):
    #         if n == target:
    #             return idx
        
    #     return -1

    # # > Single Pass Binary Search Solution: Time: O(logn), Space: O(1)
    # def search(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     left, right = 0, n-1

    #     while left <= right:
    #         mid = left + (right - left)//2
    #         if nums[mid] == target:
    #             return mid
    #         elif nums[mid] >= nums[left]:
    #             if  nums[left] <= target < nums[mid]:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1
    #         else:
    #             if nums[mid]

    #     return -1






    # # > Two Pass Binary Search Solution: Time: O(logn)
    # def search(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     left, right = 0, n-1

    #     # Boundary Binary Search: Time: O(logn)
    #     while left < right: 
    #         mid = left + (right - left)//2

    #         if nums[mid]<=nums[-1]:
    #             right = mid
    #         else:
    #             left = mid + 1

    #     # Minima index is given by this right and left
    #     minimaidx = right

    #     # Now we have to perform binary in one of the two sorted arrays.
    #     if target >= nums[minimaidx] and target <= nums[-1]:
    #         left, right = minimaidx, n-1
    #     else:
    #         left, right = 0, minimaidx-1

    #     # Exact Binary Search: Time: O(logn)
    #     while left <= right:
    #         mid = left + (right-left)//2

    #         if nums[mid] == target:
    #             return mid
    #         elif nums[mid] > target:
    #             right = mid -1
    #         else:
    #             left = mid + 1

    #     return -1
        