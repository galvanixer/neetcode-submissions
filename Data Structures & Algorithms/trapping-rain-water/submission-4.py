class Solution:

    # > Brute Force Solution: Time: O(n^2), Space: O(1)
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        for i in range(n):
            lmax, rmax = 0,0
            for j in range(n):
                lmax = max(height[j], lmax) if j<=i else lmax
                rmax = max(height[j], rmax) if j>=i else rmax
            
            water += min(lmax, rmax) - height[i]
            

        return water

    # > Prefix Suffix Solution: Time: O(n), Space: O(n)
    # def trap(self, height: List[int]) -> int:
    #     n = len(height)
    #     suffix = [0]*n
    #     prefix = [0]*n
    #     # Prefix estimation
    #     for i in range(n):
    #         prefix[i] = max(height[i], prefix[i-1]) if i>0 else height[i]

    #     for j in range(n-1,-1,-1):
    #         suffix[j] = max(height[j], suffix[j+1]) if j<n-1 else height[j]

    #     water = 0
    #     for (p,s,h) in zip(prefix, suffix, height):
    #         water += (min(p,s)-h)

    #     return water

    # # > Optimal Solution (Two Pointer Based): Time: O(n), Space: O(1)
    # def trap(self, height: List[int]) -> int:
    #     n = len(height)
    #     l, r = 0, n-1
    #     lmax, rmax = height[l], height[r]
    #     water = 0

    #     while l < r:
    #         if lmax < rmax:
    #             l += 1
    #             lmax = max(height[l], lmax)
    #             water += lmax - height[l]
    #         elif rmax <= lmax: 
    #             r -= 1
    #             rmax = max(height[r], rmax)
    #             water += rmax - height[r]

    #     return water




        