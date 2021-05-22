class Solution {
public:
    int solution1(vector<vector<int>>& grid){
        int m = grid.size();
        int n = grid[0].size();
        int dp[m][n];
        
        memset(dp, 0, sizeof(dp));
            
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                
                if(grid[i][j])  //if obstacle-->ignore further computations
                    continue;
                if(i == 0 && j == 0)
                    dp[i][j] = 1;
                else if(i == 0)
                    dp[i][j] += dp[i][j-1];
                else if(j == 0) 
                    dp[i][j] += dp[i-1][j];
                else
                    dp[i][j] += dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
    
    int solution2(vector<vector<int>>& grid){
        int m = grid.size();
        int n = grid[0].size();
        
        // if start or end has obstacle-->return 0
        if(grid[0][0] == 1 || grid[m-1][n-1] == 1)
            return 0;
        
        //num of ways to reach start = no way
        grid[0][0] = 1;
        
        //for 0th column
        for(int i = 1; i < m; i++){
            if(grid[i][0] == 0 && grid[i-1][0] == 1)
                grid[i][0] = 1;
            else
                grid[i][0] = 0;
        }
        
        //for 0th row
        for(int i = 1; i < n; i++){
            if(grid[0][i] == 0 && grid[0][i-1] == 1)
                grid[0][i] = 1;
            else
                grid[0][i] = 0;
        }
        
        //start calculations from grid[1][1]
        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++){
                //if no obstacle at grid[i][j]
                if(grid[i][j] == 0){
                    grid[i][j] = grid[i-1][j] + grid[i][j-1];
                }else {
                    //if obstacle is present make grid[i][j] = 0 so that
                    //it does not contribute to any other path
                    grid[i][j] = 0;
                }
            }
        }
        return grid[m-1][n-1];
    }
    

    int uniquePathsWithObstacles(vector<vector<int>>& grid) {
        // return solution1(grid);
        return solution2(grid);
    }    
};