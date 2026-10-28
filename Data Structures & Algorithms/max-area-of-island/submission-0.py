class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(m * n)
        # Space Complexity: O(1)

        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            for x, y in directions:
                area += dfs(r + x, c + y)
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area
            