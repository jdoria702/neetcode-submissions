class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        Min Heap
        
        - Sort tasks by enqueueTime so that we can add to heap by enqueueTime increasing
        - Python will sort by second value of tuple if there is a tie
        - Also does that with heaps
        - Maintain jobs with shortest time at the top of heap
        - Add task to heap when it is available

        """
        ### DEFINITIONS ###
        # tasks[i] = [enqueueTimei, processingTimei]
        # enqueueTimei = available to process at this time
        # processingTimei = take this much time to finish processing

        ### CONSTRAINTS ###
        # Single-threaded CPU that can process AT MOST ONE task at a time
        # If CPU is idle and tasks are available, CPU  will choose the SHORTEST task
            # If multiple have same processing time, choose the SMALLEST INDEX
        
        res = []
        heap = []
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort()

        i = 0
        time = 0
        while len(res) < len(tasks):
            # Pop task with the shortest time to complete
            if heap:
                popped = heapq.heappop(heap)
                passedTime = popped[0]
                idx = popped[1]

                time = time + passedTime
                res.append(idx)
            else:
                time = tasks[i][0]

            # Add all available jobs to heap
            while i < len(tasks) and tasks[i][0] <= time:
                TTC = tasks[i][1]
                idx = tasks[i][2]
                heapq.heappush(heap, (TTC, idx))
                i = i + 1
        
        return res
