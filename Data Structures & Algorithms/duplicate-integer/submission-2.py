class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}

        for i in nums:
            mp[i] = 1 + mp.get(i, 0) 

        for i in mp.items():
            if i[1] > 1:
                return True

        return False 