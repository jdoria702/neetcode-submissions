class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        res = -1
        while start <= end:
            middle = (start + end) // 2
            square = middle * middle
            if square > x:
                end = middle - 1
            elif square < x:
                res = middle
                start = start + 1
            else:
                return middle

        return res