class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        bucket_freq = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket_freq[freq].append(num)
        
        res = []
        for i in range(len(bucket_freq) - 1, -1, -1):
            for j in range(len(bucket_freq[i])):
                res.append(bucket_freq[i][j])
                if len(res) == k:
                    return res