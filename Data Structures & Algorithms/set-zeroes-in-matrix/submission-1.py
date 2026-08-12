class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_col_zero = False
        first_row_zero = False

        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True

        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0