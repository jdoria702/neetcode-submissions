class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for i in range(len(nums)):
            count_map[nums[i]] = count_map.get(nums[i], 0) + 1

        sorted_count_map = dict(sorted(count_map.items(), key=lambda item: item[1]))
        return list(sorted_count_map)[-k:]