class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            count = defaultdict(int)
            for val in row:
                if val != ".":
                    count[val] += 1
                    if count[val] > 1:
                        return False
        
        for c in range(len(board)):
            count = defaultdict(int)
            for r in range(len(board)):
                val = board[r][c]

                if val != ".":
                    count[val] += 1
                    if count[val] > 1:
                        return False
        
        for box in range(len(board)):
            count = defaultdict(int)
            row = (box // 3) * 3
            col = (box % 3) * 3

            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    val = board[r][c]
                    if val != '.':
                        count[val] += 1
                        if count[val] > 1:
                            return False

        return True