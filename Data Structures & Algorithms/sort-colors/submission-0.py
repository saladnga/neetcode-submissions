class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time complexity: O(n)
        # Space complexity: O(1)

        count = [0, 0, 0]
        for n in nums:
            count[n] += 1
        
        i = 0
        for n in range(len(count)):
            for j in range(count[n]):
                nums[i] = n
                i += 1