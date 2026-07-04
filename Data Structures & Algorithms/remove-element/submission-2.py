class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Use nums[:] to modify array in-place
        nums[:] = [x for x in nums if x != val]
        return len(nums)