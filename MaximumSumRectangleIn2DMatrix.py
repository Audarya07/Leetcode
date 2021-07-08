# GFG problem DP-27(Hard)
# https://www.geeksforgeeks.org/maximum-sum-rectangle-in-a-2d-matrix-dp-27/

# Input : [[2,1,-3,-4,5],[0,6,3,4,1],[2,-2,-1,4,-5],[-3,3,1,0,3]]
# Output: (18, [[6, 3, 4], [-2, -1, 4], [3, 1, 0]])

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]]) :
        curr_sum = 0
        max_sum = 0
        mx_left = 0
        mx_right = 0
        mx_up = 0
        mx_down = 0
        
        def kadane(arr):
            maxx = float('-inf')
            curr = 0
            start = 0
            end = 0
            s = 0
            for i in range(len(arr)):
                curr += arr[i]
                if curr > maxx:
                    maxx = curr
                    start = s
                    end = i
                if curr < 0:
                    curr = 0
                    s += 1
            return maxx, start, end

        for l in range(len(matrix[0])):
            arr = [0]*len(matrix)
            for r in range(l, len(matrix[0])):
                for i in range(len(matrix)):
                    arr[i] += matrix[i][r]
                    
                kd_sum, up, down = kadane(arr)
                curr_sum = kd_sum
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    mx_left = l
                    mx_right = r
                    mx_up = up
                    mx_down = down
        
        ans = []
        for i in range(mx_up, mx_down+1):
            temp = []
            for j in range(mx_left, mx_right+1):
                temp.append(matrix[i][j])
            ans.append(temp)
        return max_sum, ans