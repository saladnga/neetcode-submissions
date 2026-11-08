class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Time Complexity: O(m * n)
        # Space Complexity: O(n)

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        def dp(rows, cols):
            prevRows = [0] * cols
            for r in range(rows - 1, -1, -1):
                curRows = [0] * cols
                if obstacleGrid[r][cols - 1] == 1:
                    curRows[cols - 1] = 0
                elif r == rows - 1:
                    curRows[cols - 1] = 1
                else:
                    curRows[cols - 1] = prevRows[cols - 1]
                for c in range(cols - 2, -1, -1):
                    if obstacleGrid[r][c] == 1:
                        curRows[c] = 0
                    else:
                        curRows[c] = curRows[c + 1] + prevRows[c]
                prevRows = curRows
            return prevRows[0]

        return dp(rows, cols)