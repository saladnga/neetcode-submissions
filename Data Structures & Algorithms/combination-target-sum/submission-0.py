class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Time Complexity: O(N^T/M) - total number to the power of (target value / minimum value in nums)
        # Space Complexity: O(T/M)

        res = []

        def backtrack(idx, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if idx >= len(nums) or total > target:
                return
            curr.append(nums[idx])
            backtrack(idx, curr, nums[idx] + total)
            curr.pop()

            backtrack(idx + 1, curr, total)
            
        backtrack(0, [], 0)
        return res