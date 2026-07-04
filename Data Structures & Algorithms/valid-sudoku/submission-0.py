class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # A row is invalid if you create a set of each rule and discover
        # that the set size does not match the number of filled in cells

        # Invalid if size of set != count of nums in scenario
        
        # Rule: row does not have duplicate
        for i in range(len(board)):
            s = set(board[i])
            count = len([num for num in board[i] if num != '.'])
            if len(s) - 1 != count:
                return False

        # Rule: column does not have duplicate
        for i in range(len(board[0])):
            column = [row[i] for row in board]
            s = set(column)
            count = len([num for num in column if num != '.'])
            if len(s) - 1 != count:
                return False

        # Rule: grid does not have duplicate
        for i in range(3):
            for j in range(3):
                row = 0 + (i * 3)
                col = 0 + (j * 3)

                # add all values to grid
                grid = []
                direction = [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (1, 1), (1, 2), (2, 1), (2, 2)]
                for x, y in direction:
                    grid.append(board[row+x][col+y])
                
                s = set(grid)
                count = len([num for num in grid if num != '.'])
                if len(s) - 1 != count:
                    return False
        
        return True