class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Shift using idx + k mod len(nums)
        # Mod wraps around the array
        # ^ requires extra space
        normalized = k % len(nums)

        # Reverse array with two pointers
        l = 0
        r = len(nums) - 1
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l = l + 1
            r = r - 1
        
        # Reverse left portion
        l = 0
        r = normalized - 1
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l = l + 1
            r = r - 1

        # Reverse right portioin
        l = normalized
        r = len(nums) - 1
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l = l + 1
            r = r - 1