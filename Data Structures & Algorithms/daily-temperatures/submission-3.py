class Solution:

    # 1. Brute force solution: Time: O(n^2), Space: O(n)
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     ntemperatures = len(temperatures)
    #     out = [0]*ntemperatures
    #     for i in range(ntemperatures):
    #         curr_temp = temperatures[i]
    #         for j in range(i+1, ntemperatures):
    #             if (temperatures[j]> curr_temp):
    #                 out[i]=(j-i)
    #                 break

    #     return out

    # 2. Optimal solution using monotonic stack: Time: O(n), Space: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ntemperatures = len(temperatures)
        out = [0]*ntemperatures
        stack = []

        for (i,t) in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                out[j] = i - j
            stack.append(i)

        return out