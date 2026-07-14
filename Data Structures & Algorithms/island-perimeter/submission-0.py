class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        BFS

        - Each cell can at most provide a perimeter of 4
        - Remove 1 unit of perimeter for every island piece surrounding current cell

        """

        def bfs():
            perimeter = 0
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while q:
                popped = q.popleft()
                r = popped[0]
                c = popped[1]
                curr_perimeter = 4

                for direction in directions:
                    x = direction[0]
                    y = direction[1]

                    new_r = r + x
                    new_c = c + y

                    if new_r in range(len(grid)) and new_c in range(len(grid[0])) and grid[new_r][new_c] == 1:
                        curr_perimeter = curr_perimeter - 1
                        if (new_r, new_c) not in visited:
                            q.append((new_r, new_c))
                            visited.add((new_r, new_c))
                    
                perimeter = perimeter + curr_perimeter

            return perimeter
                        

            

        q = deque()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    q.append((r, c))
                    visited.add((r, c))
                    res = bfs()
                    return res