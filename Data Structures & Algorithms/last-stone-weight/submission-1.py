class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Maintain a maxheap to keep track of the two heaviest stones

        Pop 2 stones
        Push the absolute value of the stones subtracted
        (Do not push if stone weight is 0)

        If one stone remains in the heap return 1
        else return 0
        """

        heap = []
        for stone in stones:
            heapq.heappush(heap, -1*stone)
        
        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            combined_stone = abs(stone1 - stone2) * -1
            if combined_stone != 0:
                heapq.heappush(heap, combined_stone)
            
        if heap:
            return heap[0] * -1
        
        return 0