class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(N)

        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                return True
        return False
        