class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        # Maintain heap to size k
        # top of min heap will always have the kth largest element
        for num in nums:
            if len(self.heap) == self.k:
                heapq.heappushpop(self.heap, num)
            else:
                heapq.heappush(self.heap, num)
        

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        
        return self.heap[0]
