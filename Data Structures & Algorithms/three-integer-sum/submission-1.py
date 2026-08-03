class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        out = [] # Output list
        nums.sort() # Using this to sort in place. Time: O(n.log(n))

        # Returning empty list if the first number is greater than 0 in the sorted list.

        for i,num in enumerate(nums): # First fixed index
            if num>0:
                break
            # Removing duplication that might happen because of repeating fixed number.
            if i>0 and num == nums[i-1]:
                continue

            target = -num
            left = i+1          # left pointer
            right = n-1

            while (left<right):
                total = nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else: 
                    out.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left]==nums[left-1]:
                        left += 1

        return out



        
                
                    
        