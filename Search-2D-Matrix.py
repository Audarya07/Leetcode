class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        l = 0
        row = len(mat)
        col = len(mat[0])
        r = col - 1
        
        while l < row and r >= 0:
            if mat[l][r] == target:
                return True
            elif target > mat[l][r]:
                l += 1
            else:
                r -= 1
        return False
