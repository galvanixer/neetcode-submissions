class Solution:

    # > Optimal Solutions. Time: O(), Space: O()
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


    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
    #     left, right = 0, len(numbers)-1

    #     while left < right:

    #         if numbers[left]+numbers[right]>target:
    #             right -= 1
    #         elif numbers[left]+numbers[right]<target:
    #             left += 1
    #         else:
    #             return [left+1, right+1]

            