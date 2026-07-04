class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        length = len(nums)
        nums.sort()
        for a in range(length - 3):
            for b in range(a + 1, length - 2):
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    tot = nums[a] + nums[b] + nums[c] + nums[d]
                    if tot < target:
                        c = c + 1
                    elif tot > target:
                        d = d - 1
                    else:
                        res.add((nums[a], nums[b], nums[c], nums[d]))
                        c = c + 1
                        d = d - 1
        return [list(quad) for quad in res]