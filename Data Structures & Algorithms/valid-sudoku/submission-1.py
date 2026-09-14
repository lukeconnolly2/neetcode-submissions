class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = defaultdict(set)
        colSets = defaultdict(set)
        boxSets = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                num = board[row][col]
                if num == '.':
                    continue
                box = (row // 3, col // 3)

                seenInRow = num in rowSets[row]
                seenInCol = num in colSets[col]
                seenInBox = num in boxSets[box]


                if seenInRow or seenInCol or seenInBox:
                    return False

                rowSets[row].add(num)
                colSets[col].add(num)
                boxSets[box].add(num)
        
        return True