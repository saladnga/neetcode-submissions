class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time Complexity: O(m * n)
        # Space Complexity: O(1) - in place modification

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        total = 0

        def dfs(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for x, y in directions:
                dfs(r + x, c)
                dfs(r, c + y)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    total += 1
        
        return total