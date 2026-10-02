class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Time Complexity: O(NlogM)
        # Space Complexity: O(1)

        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            total_hours = sum(math.ceil(pile / mid) for pile in piles)
            if total_hours > h:
                low = mid + 1
            else:
                high = mid - 1
        return low