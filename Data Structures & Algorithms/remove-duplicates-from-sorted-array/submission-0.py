class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Read pointer: look for unique values
            # Keep track of last recorded value
            # If current value is different, write and save value
        # Write pointer: keeps track of where to write the unique value
            # Increment only if a unique value is written

        unique = 1
        last = nums[0]
        read = 1
        write = 1
        while read < len(nums):
            if nums[read] != last:
                nums[write] = nums[read]
                last = nums[read]

                unique = unique + 1
                read = read + 1
                write = write + 1
            else:
                read = read + 1
        return unique