class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Prefix product

        Store two prefix arrays left and right

        At l_prefix[i]:
            - represents the product of all values left of i
        At r_prefix[i]:
            - represents the product of all values right of i
        
        Multiply and store (in res) corresponding index of two arrays
        """

        l_prefix = [1] * len(nums)
        r_prefix = [1] * len(nums)

        for i in range(1, len(nums)):
            l_prefix[i] = l_prefix[i-1] * nums[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            r_prefix[i] = r_prefix[i+1] * nums[i+1]
        
        res = []
        for i in range(len(nums)):
            prod = l_prefix[i] * r_prefix[i]
            res.append(prod)
        
        return res