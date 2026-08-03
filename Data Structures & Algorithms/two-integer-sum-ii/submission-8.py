class Solution:

    # > Optimal Solutions. Time: O(n), Space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1

        while left < right:
            total = numbers[left] + numbers[right]
            if target > total:
                left += 1
            elif target < total:
                right -= 1
            else:
                return [left+1, right+1]

        return []

    # > Brute Force. Time: O(n^2), Space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n):
            for j in range(i+1, n):
                total = numbers[i]+numbers[j]
                if total == target:
                    return [i+1, j+1]

        return []


    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
    #     left, right = 0, len(numbers)-1

    #     while left < right:

    #         if numbers[left]+numbers[right]>target:
    #             right -= 1
    #         elif numbers[left]+numbers[right]<target:
    #             left += 1
    #         else:
    #             return [left+1, right+1]

            