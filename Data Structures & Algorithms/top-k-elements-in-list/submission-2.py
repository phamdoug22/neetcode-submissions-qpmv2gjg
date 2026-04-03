class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}

        for i in nums:
            mp[i] = 1 + mp.get(i, 0)
        
        arr = []
        for num, count in mp.items():
            arr.append([count, num])
        
        arr.sort()

        res = set()
        while k > 0:
            count, num = arr.pop(-1)
            k -= 1
            res.add(num)
        
        
        return list(res)