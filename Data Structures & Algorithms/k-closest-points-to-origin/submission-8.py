class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_dist(p):
            return p[0]**2 + p[1]**2
        
        def partition(l, r):
            pivot = get_dist(points[r])
            i = l
            for j in range(l, r):
                if get_dist(points[j]) <= pivot:
                    points[j], points[i] = points[i], points[j]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        
        L, R = 0, len(points) - 1
        pivot = len(points)
        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]