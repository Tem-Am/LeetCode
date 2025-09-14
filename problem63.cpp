#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        // Size of obstacleGrid
        int n = obstacleGrid.size();
        int m = obstacleGrid[0].size();

        // Edge case
        if(obstacleGrid[0][0] == 1 || obstacleGrid[n-1][m-1] == 1){
            return 0;
        }

        // Initialize first move
        obstacleGrid[0][0] = 1;

        for(int i = 1; i < n; i++){
            if(obstacleGrid[i][0] == 1){
                obstacleGrid[i][0] = 0;
            }
            else{
                obstacleGrid[i][0] = obstacleGrid[i-1][0];
            }
        }    

        for(int j = 1; j < m; j++){
            if(obstacleGrid[0][j] == 1){
                obstacleGrid[0][j] = 0;
            }
            else{
                obstacleGrid[0][j] = obstacleGrid[0][j-1];
            }
        }

        for(int row = 1; row < n; row++){
            for(int col = 1; col < m; col++){
                if(obstacleGrid[row][col] == 1){
                    obstacleGrid[row][col] = 0;
                }
                else{
                    obstacleGrid[row][col] = (obstacleGrid[row-1][col] + obstacleGrid[row][col-1]);
                }
            }
        }
        return obstacleGrid[n-1][m-1];
    }
};