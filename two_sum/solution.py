class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            n = nums[i]
            difference = target - n 

            if difference in d:
                return [i, d[difference]]

            d[n] = i

