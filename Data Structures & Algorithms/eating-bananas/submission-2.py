class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        maxpileheight = max(piles)

        # The number of bananas I can eat per hour can lie between [1, maxpileheight]
        l, r = 1, maxpileheight

        while l < r: 
            m = l + (r - l)//2 # m bananas per hour eating rate
            totalhours = 0
            for p in piles:
                totalhours += (p - 1) // m + 1

            if totalhours <= h:
                r = m
            else:
                l = m + 1

        return l


