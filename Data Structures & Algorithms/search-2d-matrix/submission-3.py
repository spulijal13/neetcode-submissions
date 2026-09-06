class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m * n - 1

        while start <= end:
            mid = (start + end) // 2
            mid_index = (mid // n, mid % n)

            if target == matrix[mid_index[0]][mid_index[1]]:
                return True
            elif target > matrix[mid_index[0]][mid_index[1]]:
                start = mid + 1
            else:
                end = mid - 1
        
        return False