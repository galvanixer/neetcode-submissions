class Solution:

    # > Prefix Suffix Solution: Time: O(), Space: O()
    def trap(self, height: List[int]) -> int:
        n = len(height)
        suffix = [0]*n
        prefix = [0]*n
        # Prefix estimation
        for i in range(n):
            prefix[i] = max(height[i], prefix[i-1]) if i>0 else height[i]

        for j in range(n-1,-1,-1):
            suffix[j] = max(height[j], suffix[j+1]) if j<n-1 else height[j]

        maxwater = 0
        for (p,s,h) in zip(prefix, suffix, height):
            maxwater += (min(p,s)-h)
            print(maxwater)

        return maxwater



































    # # > Optimal Solution: Time: O(), Space: O()
    # def trap(self, height: List[int]) -> int:

    #     n = len(height)

    #     pfxmax, sfxmax = 0, 0
    #     prefix = [0]*n
    #     suffix = [0]*n

    #     for i in range(n):
    #         pfxmax = max(height[i], pfxmax)
    #         prefix[i] = pfxmax

    #     for j in range(n-1, -1, -1):
    #         sfxmax = max(height[j], sfxmax)
    #         suffix[j]=sfxmax

    #     water = 0
    #     for i in range(n):
    #         water += max(0, min(suffix[i], prefix[i])-height[i])

    #     return water


        