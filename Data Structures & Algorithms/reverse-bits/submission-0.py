class Solution:
    def reverseBits(self, n: int) -> int:
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res