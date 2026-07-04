class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_val = 0
        while left < right:
            width = right - left
            length = min(heights[left], heights[right])
            area = width * length
            max_val = max(max_val, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_val