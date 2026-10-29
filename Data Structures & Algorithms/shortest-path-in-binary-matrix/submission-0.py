class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)

        def bfs(grid):
            ROWS, COLS = len(grid), len(grid[0])
            directions = [[1, 1], [-1, -1], [1, 0], [-1, 0], [0, -1], [0, 1], [1, -1], [-1, 1]]
            visit = set()
            queue = deque()
            visit.add((0, 0))
            queue.append((0, 0))

            if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
                return -1
            
            length = 1
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if r == ROWS - 1 and c == COLS - 1:
                        return length
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if not (0 <= nr < ROWS) or not (0 <= nc < COLS) or (nr, nc) in visit or grid[nr][nc] == 1:
                            continue
                        visit.add((nr, nc))
                        queue.append((nr, nc))
                length += 1
            return -1

        return bfs(grid)
