class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        smallest = float('inf')

        l = 0
        r = 0
        while r < len(nums):
            total = total + nums[r]
            while total >= target:
                smallest = min(r - l + 1, smallest)
                total = total - nums[l]
                l = l + 1
            
            r = r + 1
        
        if smallest == float('inf'):
            return 0
        
        return smallest