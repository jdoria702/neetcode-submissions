class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        l = 0
        r = 0
        while r < len(nums):
            if r - l > k:
                s.remove(nums[l])
                l = l + 1
            
            if nums[r] in s:
                return True
            
            s.add(nums[r])
            r = r + 1
        
        return False