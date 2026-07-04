class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = deque()
        for i in range(k):
            q.append((arr[i], abs(x - arr[i])))
        
        l = 1
        r = k
        while r < len(arr):
            candidate = arr[r]
            candidate_dist = abs(x - candidate)

            if candidate_dist < q[0][1]:
                q.popleft()
                q.append((candidate, candidate_dist))
            elif candidate == q[0][0]:
                q.popleft()
                q.append((candidate, candidate_dist))
            else:
                break
            
            r = r + 1
        
        res = []
        for tup in q:
            res.append(tup[0])
        
        return res