class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. Brute force
        n = len(numbers)
        for idx1 in range(n):
            diff = target - numbers[idx1]
            for idx2 in range(idx1,n):
                if numbers[idx2]==diff:
                    return [idx1+1, idx2+1]
