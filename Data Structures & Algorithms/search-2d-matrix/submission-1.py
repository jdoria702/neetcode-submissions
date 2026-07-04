class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = []

        # Find the row target is in
        # O(n)
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                row = matrix[i]
                break
        
        if not row:
            return False
        
        # Binary search on array
        l = 0
        r = len(row) - 1
        while l < r:
            middle = (l + r) // 2
            
            if row[middle] == target:
                return True
            
            if target > row[middle]:
                l = middle + 1
            else:
                r = middle - 1
        
        if l == r and row[l] == target:
            return True
        
        return False