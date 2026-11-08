class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Time Complexity: O(m * n)
        # Space Complexity: O(n)

        m, n = len(text1), len(text2)
        def dp(m, n):
            prevRows = [0] * (n + 1)
            for r in range(m - 1, -1, -1):
                curRows = [0] * (n + 1)
                for c in range(n - 1, -1, -1):
                    if text1[r] != text2[c]:
                        curRows[c] = max(prevRows[c], curRows[c + 1])
                    else:
                        curRows[c] = 1 + prevRows[c + 1]
                prevRows = curRows
            return prevRows[0]
        return dp(m, n)