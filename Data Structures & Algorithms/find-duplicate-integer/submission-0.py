class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = {}

        for i in nums:
            mp[i] = 1 + mp.get(i, 0)
        
        for key in mp:
            if mp[key] > 1:
                return key
        