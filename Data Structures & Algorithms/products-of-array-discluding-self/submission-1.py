class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero_cnt = 1, 0

        for num in nums:
            if num:
                product *= num
            else:
                zero_cnt += 1
        if zero_cnt >= 2:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        
        if zero_cnt > 1:
            return [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt > 0:
                if c == 0:
                    res[i] = product
                else:
                    res[i] = 0
            else:
                res[i] = product // c
        return res