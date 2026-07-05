class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle_idx = (end + start) // 2
            if nums[middle_idx] == target:
                return middle_idx
            elif nums[middle_idx] < target:
                start = middle_idx + 1
            else:
                end = middle_idx - 1
        return -1
