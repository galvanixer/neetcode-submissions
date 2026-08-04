class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # > Brute Force Solution. Time: O(), Space: O()
        n = len(heights)
        
        maxarea = 0
        for i in range(n):
            minheight = heights[i]
            for j in range(i,n):
                minheight = min(minheight, heights[j])
                area = (j-i+1)*minheight
                maxarea = max(area, maxarea)

        return maxarea