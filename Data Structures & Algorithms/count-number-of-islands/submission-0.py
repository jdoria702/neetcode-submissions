class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs():
            while q:
                r, c = q.popleft()
                
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for direction in directions:
                    x, y = direction
                    new_r = r + x
                    new_c = c + y

                    if new_r >= 0 and new_r < len(grid) and  new_c >=0 and new_c < len(grid[0]) and grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))

        q = deque()
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    count = count + 1
                    q.append((r,c))
                    visited.add((r, c))
                    bfs()

        return count