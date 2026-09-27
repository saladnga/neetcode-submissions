class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        left, right = 0, len(matrix) - 1
        chosen_row = []
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                chosen_row = matrix[mid]
                break
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        if chosen_row:
            low, high = 0 , len(chosen_row) - 1
            while low <= high:
                mid = (low + high) // 2
                if target == chosen_row[mid]:
                    return True
                elif target < chosen_row[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False