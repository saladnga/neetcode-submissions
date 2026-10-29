class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)

        def bfs(grid):
            ROWS, COLS = len(grid), len(grid[0])
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            queue = deque()
            
            fresh = 0
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1:
                        fresh += 1
                    elif grid[r][c] == 2:
                        queue.append((r, c))
            
            minutes = 0
            while fresh > 0 and queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if not (0 <= nr < ROWS) or not (0 <= nc < COLS) or grid[nr][nc] != 1:
                            continue
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
                minutes += 1

            return minutes if fresh == 0 else -1
        
        return bfs(grid)
