class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # At each cell add the prefix of the square above and the prefix of the row to the left
        # Add current + prefixNums[above] + prefix

        # O(n^2) initialization
        self.prefixNums = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            prefix = 0
            for j in range(len(matrix[0])):
                self.prefixNums[i+1][j+1] = matrix[i][j] + self.prefixNums[i][j+1] + prefix
                prefix = prefix + matrix[i][j]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # return the bottom right of the rectangle
        # minus [row2][col1 - 1] (bottom left left)
        # minus [row1 - 1][col2] (top right top)
        # add [row1 - 1][col1 - 1] (top left top left)
        # NOTE: this is in reference to the matrix NOT the prefixNums

        # O(1) operations
        whole = self.prefixNums[row2+1][col2+1]
        left = self.prefixNums[row2+1][col1]
        top = self.prefixNums[row1][col2+1]
        readd = self.prefixNums[row1][col1]

        return whole - left - top + readd


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
