class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        count = 0
        while n:
            count += 1 if n & 1 else 0
            n >>= 1
        return count