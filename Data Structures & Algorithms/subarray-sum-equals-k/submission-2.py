class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [2, 1, 2, 4]
        # Store prefix sums
        # while storing prefix nums:
            # check in counter if there exists a prefix such that
            # current prefix - counter[key].get = k
        prefix = 0
        res = 0
        count = {}
        count[0] = 1
        for i in range(len(nums)):
            prefix = prefix + nums[i]
            
            # valid_key is the corr key that makes prefix - valid_key = k
            valid_key = prefix - k
            if valid_key in count:
                res = res + count[valid_key]
            
            count[prefix] = count.get(prefix, 0) + 1
            
        return res
