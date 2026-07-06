class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        min_capacity = end
        while start <= end:
            capacity = (start + end) // 2

            completed_days = 0
            curr_weight = 0
            for weight in weights:
                if curr_weight + weight > capacity:
                    curr_weight = weight
                    completed_days = completed_days + 1
                else:
                    curr_weight = curr_weight + weight
            
            completed_days = completed_days + 1

            if completed_days <= days:
                end = capacity - 1
                min_capacity = min(min_capacity, capacity)
            else:
                start = capacity + 1
        
        return min_capacity