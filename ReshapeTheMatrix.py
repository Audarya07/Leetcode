class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(nums)
        col = len(nums[0])
        
        if row*col != r*c:
            return nums
        
        res =[ [ 0 for i in range(c)] for j in range(r)] 
        tmp = []
        for i in range(row):
            for j in range(col):
                tmp.append(nums[i][j])
        
        x = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = tmp[x]
                x += 1
                    
        return res
