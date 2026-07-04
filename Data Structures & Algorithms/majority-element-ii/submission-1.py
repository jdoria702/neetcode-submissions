class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Add counter
        # If size of counter == 3
            # Decrement each value by 1
            # If value == 0, remove the key
        # At the end of the pass, count all occurrences of key
        # If they pass threshold, it is part of answer
        
        threshold = len(nums) // 3
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if len(count) == 3:
                to_delete = []
                for k, v in count.items():
                    count[k] = count[k] - 1
                    if count[k] == 0:
                        to_delete.append(k)
                for key in to_delete:
                    count.pop(key)

        res = []
        for k, v in count.items():
            if nums.count(k) > threshold:
                res.append(k)
        
        return res
        