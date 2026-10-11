class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time Complexity: O(NlogK)
        # Space Complexity: O(K)
        
        def get_dist(p):
            return p[0]**2 + p[1]**2
        max_heap = []
        for p in points:
            heapq.heappush(max_heap, [-get_dist(p), p])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [p for dist, p in max_heap]