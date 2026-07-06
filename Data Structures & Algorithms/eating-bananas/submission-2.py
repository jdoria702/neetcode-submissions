class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        ret = end
        while start <= end:
            middle = (end + start) // 2
            time = 0
            for pile in piles:
                time = time + math.ceil(pile / middle)
            
            print(time)
            if time <= h:
                ret = min(ret, middle)
                end = middle - 1
            else:
                start = middle + 1
        
        return ret