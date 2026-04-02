class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_cnt = 0

        for n in nums:
            if n == 0:
                zero_cnt += 1
            else:
                product *= n

        if zero_cnt > 1:
            return [0] * len(nums)

        res = []
        for n in nums:
            if zero_cnt == 1:
                res.append(product if n == 0 else 0)
            else:
                res.append(product // n)

        return res