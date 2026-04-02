class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[mid][0] <= target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
                
        row = r

        l, r = 0, len(matrix[mid]) - 1

        while l <= r:
            mid_two = l + (r - l) // 2
            if matrix[row][mid_two] < target:
                l = mid_two + 1
            elif matrix[row][mid_two] > target:
                r = mid_two - 1
            else:
                return True
        return False