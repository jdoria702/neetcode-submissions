class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2

            # check middle value
            if nums[middle] == target:
                return middle
            
            # target is more than middle
            if target > nums[middle]:
                left = middle + 1
            
            # target is less than middle
            else:
                right = middle - 1

        if left == right and nums[left] == target:
            return left

        return -1