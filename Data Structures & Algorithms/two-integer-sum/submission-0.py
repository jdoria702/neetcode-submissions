class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in hmap:
                return [hmap[key], i]
            hmap[nums[i]] = i
        return