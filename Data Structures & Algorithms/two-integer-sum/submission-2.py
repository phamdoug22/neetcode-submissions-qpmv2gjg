class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for j, k in enumerate(nums):
            diff = target - k
            if diff in prevMap:
                return [prevMap[diff], j]
            prevMap[k] = j