class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = -1
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j - i
                length = min(heights[i], heights[j])
                res = max(res, width * length)
        return res