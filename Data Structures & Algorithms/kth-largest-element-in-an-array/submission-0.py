class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        pop_till = len(max_heap) - k + 1

        while len(max_heap) > pop_till:
            heapq.heappop(max_heap)
        
        return -max_heap[0]