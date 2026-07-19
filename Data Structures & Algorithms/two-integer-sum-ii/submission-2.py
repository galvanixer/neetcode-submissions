class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # 1. Brute force
        # n = len(numbers)
        # for idx1 in range(n):
        #     diff = target - numbers[idx1]
        #     for idx2 in range(idx1,n):
        #         if numbers[idx2]==diff:
        #             return [idx1+1, idx2+1]
        # return []

        # 2. Let's do Binary Search (since the array is already sorted.)
        n = len(numbers)
        for idx1 in range(n):
            diff = target - numbers[idx1]
            left, right = idx1+1, (n-1)
            while left <= right:
                middle = (left + right) // 2
                if numbers[middle]==diff:
                    return [idx1+1, middle+1]
                if numbers[middle] < diff:
                    left = middle + 1
                else:
                    right = middle - 1

        return []