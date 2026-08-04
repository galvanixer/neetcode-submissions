class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        nfleets = 0
        prev = 0
        # Time: O(nlogn), Space: O(n)
        pssorted = sorted(zip(position, speed), reverse=True) # Sorted pos+speed in descending order.

        for (p,s) in pssorted:
            t = (target-p)/s
            if t > prev:
                nfleets += 1
                prev = t

        return nfleets


        
