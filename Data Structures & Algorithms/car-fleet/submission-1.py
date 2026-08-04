class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ncars = len(position)
        time = [0]*ncars
        
        # Time: O(nlogn), Space: O(n)
        pssorted = sorted(zip(position, speed), reverse=True) # Sorted pos+speed in descending order.

        # Time: O(n), Space: O(1)
        for (i, (p,s)) in enumerate(pssorted):
            time[i] = ((target-p)/s)

        ncarfleets = 0

        cuttingtime = time[0]
        ncarfleet = 1
        for t in time:
            if t> cuttingtime:
                ncarfleet += 1
                cuttingtime = t

        return ncarfleet


        
