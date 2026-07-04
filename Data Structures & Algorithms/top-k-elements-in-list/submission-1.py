class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time O(n): iterate through array once
        # Space O(m): where m is the distinct elements in the array
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        # get key with largest values
        k_frequent = []
        for _ in range(k):
            largest_key = max(hmap, key=hmap.get)
            k_frequent.append(largest_key)
            hmap.pop(largest_key, None)
        
        return k_frequent