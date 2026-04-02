class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2

            total = 0
            for p in piles:
                total += (p + mid - 1) // mid

            if total <= h:
                r = mid
            else:
                l = mid + 1

        return l