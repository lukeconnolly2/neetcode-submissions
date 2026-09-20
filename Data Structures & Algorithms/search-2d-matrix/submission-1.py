class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        row = None
        while top <= bottom:
            mid = (top + bottom) // 2

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            elif target <= matrix[mid][-1] and target >= matrix[mid][0]:
                row = matrix[mid]
                break
            else: 
                return False
        
        if not row:
            return False

        l, r = 0, len(row)
        while l <= r:
            m = (l + r) // 2

            if target < row[m]: 
                r = m - 1
            elif target > row[m]:
                l = m + 1
            else:
                return True

        return False
