class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print(sorted_nums)

        # Case: all numbers are zero
        if sorted_nums[0] == 0 and sorted_nums[-1] == 0:
            return [[0, 0, 0]]

        # Case: all nums are negative or positive (impossible to make 0)
        if (sorted_nums[0] <= 0 and sorted_nums[-1] <= 0) or (sorted_nums[0] >= 0 and sorted_nums[-1] >= 0):
            return []

        res = []
        for l in range(len(sorted_nums)):
            if l > 0 and sorted_nums[l] == sorted_nums[l - 1]:
                continue

            m = l + 1
            r = len(sorted_nums) - 1

            while m < r:
                if sorted_nums[l] + sorted_nums[m] + sorted_nums[r] == 0:
                    res.append([sorted_nums[l], sorted_nums[m], sorted_nums[r]])
                    
                    while m < r and sorted_nums[m] == sorted_nums[m + 1]:
                        m = m + 1

                    while m < r and sorted_nums[r] == sorted_nums[r - 1]:
                        r = r - 1

                    m = m + 1
                    r = r - 1
                    continue
                
                if sorted_nums[l] + sorted_nums[m] + sorted_nums[r] < 0:
                    m = m + 1
                else:
                    r = r - 1

        return res
                    