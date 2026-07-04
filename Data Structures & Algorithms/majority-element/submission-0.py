class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Keep count of majority value
        # Increase count if majority value seen
        # Decrease count if majority value not seen
        majority = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == majority:
                count = count + 1
            else:
                count = count - 1
                if count == 0:
                    majority = nums[i]
                    count = count + 1
        return majority