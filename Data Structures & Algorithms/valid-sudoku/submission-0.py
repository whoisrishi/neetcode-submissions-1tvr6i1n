class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            filtered = [x for x in row if x != '.']
            if len(filtered) != len(set(filtered)):
                return False
        
        for col in zip(*board):
            filtered = [x for x in col if x != '.']
            if len(filtered) != len(set(filtered)):
                return False
        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                square = [
                    board[i][j] 
                    for i in range(r, r + 3) 
                    for j in range(c, c + 3)
                ]
                filtered = [x for x in square if x != '.']
                if len(filtered) != len(set(filtered)):
                    return False
        
        return True
