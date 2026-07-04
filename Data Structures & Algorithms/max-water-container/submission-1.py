class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = -1
        left = 0
        right = len(heights) - 1
        while left < right:
            length = min(heights[left], heights[right])
            width = right - left
            res = max(res, length * width)

            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1

        return res