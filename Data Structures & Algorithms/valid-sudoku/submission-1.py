from math import isqrt

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # generalizing for an N*N sudoku matrix with optimization 
        # assumption matrix is a perfect square N*N 
        n = len(board)
        box = isqrt(n)

        rows = [0] * n
        cols = [0] * n
        sqrs = [0] * n

        for row in range(n):
            for col in range(n): 
                
                val = board[row][col]
                
                # check if the cell is empty first
                if  val == ".":
                    continue 
                
                # create bit mask and box index
                bit_mask = 1 << (int(val) - 1)
                box_idx = (row // box) * box + (col // box)
                
                # check if number is repeated using bitwise and 
                if (rows[row] &  bit_mask or 
                    cols[col] & bit_mask or 
                    sqrs[box_idx] & bit_mask):
                    return False
                
                rows[row] |= bit_mask
                cols[col] |= bit_mask
                sqrs[box_idx] |=bit_mask
        
        return True



