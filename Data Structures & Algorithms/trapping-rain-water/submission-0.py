class Solution:

    # > Optimal Solution: Time: O(), Space: O()
    def trap(self, height: List[int]) -> int:

        n = len(height)

        pfxmax, sfxmax = 0, 0
        prefix = [0]*n
        suffix = [0]*n

        for i in range(n):
            pfxmax = max(height[i], pfxmax)
            prefix[i] = pfxmax

        for j in range(n-1, -1, -1):
            sfxmax = max(height[j], sfxmax)
            suffix[j]=sfxmax

        water = 0
        for i in range(n):
            water += max(0, min(suffix[i], prefix[i])-height[i])

        return water


        