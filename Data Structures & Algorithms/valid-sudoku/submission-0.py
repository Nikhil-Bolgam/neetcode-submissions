from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)


    
        for row in range(len(board)):
            for col in range(len(board[0])):

                # check if it can conitnue 
                if board[row][col] == ".":
                    continue
                
                # check if it is in any of the sets to fail
                elif( (board[row][col] in rows[row]) or 
                    (board[row][col] in cols[col]) or 
                    (board[row][col] in sqrs[(row//3, col//3)])
                    ):
                    return False 
                
                # if not seen to fail update the sets for new elements
                else :
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col]) 
                    sqrs[(row//3, col//3)].add(board[row][col])
        return True

