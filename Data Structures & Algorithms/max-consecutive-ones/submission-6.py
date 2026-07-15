class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        curr = 0
        for num in nums:
            if num != 1:
                max_count = max(max_count, curr)
                curr = 0
            else:
                curr += 1
        return max(max_count, curr)