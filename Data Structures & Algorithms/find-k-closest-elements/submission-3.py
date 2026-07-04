class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = k
        while r < len(arr):
            candidate = arr[r]
            candidate_dist = abs(x - candidate)

            if candidate_dist < abs(arr[l] - x):
                l = l + 1
            elif candidate == arr[l]:
                l = l + 1
            else:
                break
            
            r = r + 1
        
        return arr[l:r]