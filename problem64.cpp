#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        // This is DP problem
        // Need n and m of grid 
        int n = grid.size();
        int m = grid[0].size();

        // Change all numbers in first row and col 
        for(int i = 1; i < n; i++){
            grid[i][0] += grid[i-1][0];
        }

        for(int j =1; j < m; j++){
            grid[0][j] += grid[0][j-1];
        }

        for(int row = 1; row < n; row++){
            for(int col = 1; col < m; col++){
                grid[row][col] += min(grid[row-1][col], grid[row][col-1]);
            }
        }

        return grid[n-1][m-1];
    }
};