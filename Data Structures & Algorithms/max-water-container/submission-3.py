class Solution:

    # > Brute Force. Time: O(n^2), Space: O(1)
    # def maxArea(self, heights: List[int]) -> int:

    #     n = len(heights)
    #     maxwater = 0

    #     for i in range(n):
    #         for j in range(i, n):
    #             water = min(heights[i], heights[j])*(j-i)
    #             maxwater = max(maxwater, water)

    #     return maxwater

    # > Optimal Solution. Time: O(), Space: O()
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        maxwater = 0

        left, right = 0, n-1
        
        while left < right:
            hr = heights[right]
            hl = heights[left]
            water = (right-left)*min(hl,hr)
            maxwater = max(maxwater, water)

            if hl < hr:
                while left<right and heights[left]<=hl:
                    left+=1
            else:
                while left<right and heights[right]<=hr:
                    right-=1

        return maxwater





        