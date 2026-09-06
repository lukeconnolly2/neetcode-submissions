class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BOARD_SIZE = 9

        rowSeen = collections.defaultdict(set)
        colSeen = collections.defaultdict(set)
        squareSeen = collections.defaultdict(set)

        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                currentCell = board[r][c]
                if currentCell == '.':
                    continue
                
                squareIndex = (r // 3, c // 3)

                hasBeenSeenInRow = currentCell in rowSeen[r]
                hasBeenSeenInCol = currentCell in colSeen[c]
                hasBeenSeenInSquare = currentCell in squareSeen[squareIndex]

                if hasBeenSeenInRow or hasBeenSeenInCol or hasBeenSeenInSquare:
                    return False
                
                rowSeen[r].add(currentCell)
                colSeen[c].add(currentCell)
                squareSeen[squareIndex].add(currentCell)
        
        return True
                