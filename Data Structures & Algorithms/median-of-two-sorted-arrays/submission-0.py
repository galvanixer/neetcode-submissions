class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # > Brute Force Solution. Time: 
        nums = sorted(nums1 + nums2) # Time:O((n+m)log(n+m)) Space: O(n+m)
        n = len(nums)
        mid = n//2
        if n % 2 == 0:
            return (nums[mid]+nums[mid-1])/2
        else:
            return nums[mid]