class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Monotonically increasing stack
        Entries represent rectangles that can still be built on
        """

        # (height, position)
        stack = []
        largest = 0
        for i, height in enumerate(heights):
            if not stack or stack[-1][0] <= height:
                stack.append((height, i))
                continue

            while stack and stack[-1][0] > height:
                popped = stack.pop()
                area = (i - popped[1]) * popped[0]
                largest = max(largest, area)

            stack.append((height, popped[1]))
        
        x = len(heights)
        while stack:
            popped = stack.pop()
            area = (x - popped[1]) * popped[0]
            largest = max(largest, area)
        
        return largest