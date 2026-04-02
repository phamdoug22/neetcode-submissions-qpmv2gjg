class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # need to compare previous iterations of area calc

        l, r = 0, len(heights) - 1
        current_max = 0

        while l < r:
            min_bar = min(heights[l], heights[r])
            area = min_bar * (r - l)
            current_max = max(current_max, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return current_max