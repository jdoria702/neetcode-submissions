class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) - 1
        
        # add each value into a minheap
        # python does not support max heap so we wiil use negative values
        heap = []
        for _, v in count.items():
            heapq.heappush(heap, v)
        
        q = deque()
        time = 0

        # Tuples will be added to queue
        # (Remaining value, time to completion)
        while heap or q:
            time = time + 1
            # print("heap and q before: ")
            # print(heap)
            # print(q)
            if heap:
                largest = heapq.heappop(heap) + 1
                if largest < 0:
                    # print("ADDED TO Q: ", (largest, time + n))
                    q.append((largest, time + n))
            if q and q[0][1] == time:
                tup = q.popleft()
                heapq.heappush(heap, tup[0])

            # print("heap and q after: ")
            # print(heap)
            # print(q)
            
        return time