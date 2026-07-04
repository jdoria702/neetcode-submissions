class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        original_size = len(nums)
        nums[:] = [x for x in nums if x != val]
        print(nums)
        print(original_size - len(nums))
        return len(nums)