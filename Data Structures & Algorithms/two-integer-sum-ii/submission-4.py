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

        # # 2. Let's do Binary Search (since the array is already sorted.)
        # n = len(numbers)
        # for idx1 in range(n):
        #     diff = target - numbers[idx1]
        #     left, right = idx1+1, (n-1)
        #     while left <= right:
        #         middle = (left + right) // 2
        #         if numbers[middle]==diff:
        #             return [idx1+1, middle+1]
        #         if numbers[middle] < diff:
        #             left = middle + 1
        #         else:
        #             right = middle - 1

        # return []
        
        # # 3. Hash Map (Solution)
        # targetdict = {}

        # for (idx, num) in enumerate(numbers):
        #     diff = target - num
        #     if diff in targetdict:
        #         return [targetdict[diff]+1, idx+1]
        #     targetdict[num]=idx

        # return []

        # 4. Two Pointers (New Strategy. Somehow we do not need a hash map as things are sorted)
        left = 0 # Left pointer
        right = len(numbers)-1

        while (left < right):
            currsum = numbers[left] + numbers[right]
            if currsum > target:
                right -= 1
            if currsum < target:
                left += 1
            if currsum == target:
                return [left+1, right+1]

        return []



