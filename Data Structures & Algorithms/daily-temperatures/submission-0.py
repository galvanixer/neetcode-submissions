class Solution:

    # Brute force solution: O(n^2)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ntemperatures = len(temperatures)
        out = [0]*ntemperatures
        for i in range(ntemperatures):
            curr_temp = temperatures[i]
            for j in range(i+1, ntemperatures):
                if (temperatures[j]> curr_temp):
                    out[i]=(j-i)
                    break

        return out