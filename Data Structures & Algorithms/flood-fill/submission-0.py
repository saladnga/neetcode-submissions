class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)

        if image[sr][sc] == color:
            return image
        ROWS, COLS = len(image), len(image[0])
        original = image[sr][sc]

        def dfs(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or image[r][c] != original:
                return
            else:
                image[r][c] = color
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        dfs(sr, sc)
        return image
