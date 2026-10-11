class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time Complexity: O(NlogN)
        # Space Complexity: O(N)
        
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            val1 = -heapq.heappop(stones)
            val2 = -heapq.heappop(stones)
            if val1 != val2:
                heapq.heappush(stones, -(abs(val1 - val2)))
            else:
                continue
        return -stones[0] if stones else 0