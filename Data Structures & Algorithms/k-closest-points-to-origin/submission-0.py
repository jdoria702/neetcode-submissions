class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Min Heap

        Calculate distance for each point and store in min heap
        Each node will store:
            (dist, [x, y])
        
        Pop k items from heap and store in return list
        """

        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = math.sqrt(x**2 + y**2) * -1
            
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, [x, y]))
            else:
                heapq.heappush(heap, (dist, [x, y]))

            
        res = []
        while heap:
            popped = heapq.heappop(heap)
            coord = popped[1]
            res.append(coord)

        return res