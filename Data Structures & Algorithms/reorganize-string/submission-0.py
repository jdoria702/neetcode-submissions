class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) - 1
        
        heap = []
        for k, v in count.items():
            heapq.heappush(heap, (v, k))
        
        q = deque()
        res = ""
        while heap:
            freq, char = heapq.heappop(heap)
            res = res + char
            freq = freq + 1

            if q:
                heapq.heappush(heap, q.popleft())

            if freq < 0:
                q.append((freq, char))

        if q:
            return ""

        return res