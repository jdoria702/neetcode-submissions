class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        lmax = height[0]
        rmax = height[-1]

        l = 0
        r = len(height) - 1
        while l < r:
            if lmax <= rmax:
                l = l + 1
                if lmax - height[l] > 0:
                    print("left: ", l)
                    total_water = total_water + lmax - height[l]
                if height[l] > lmax:
                    lmax = height[l]
            else:
                r = r - 1
                if rmax - height[r] > 0:
                    print("right: ", r)
                    total_water = total_water + rmax - height[r]
                if height[r] > rmax:
                    rmax = height[r]
        return total_water