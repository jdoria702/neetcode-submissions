class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, num in enumerate(nums):
            key_needed = target - num
            if hmap.get(key_needed) != None:
                return [hmap.get(key_needed), i]
            else:
                hmap[num] = i