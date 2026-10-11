class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time Complexity: O(NlogN)
        # Space Complexity: O(K)

        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]