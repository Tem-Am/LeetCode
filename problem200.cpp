#include <vector>
#include <set>
#include <iostream>
using namespace std;

class Solution {
public:
    // where set for visited lands
    set<vector<int>> visited;

    // this is dfs problem
    void dfs(int row, int col, vector<vector<char>>& grid ){
        // add to visited set
        visited.insert({row, col});
        // check top
        if(row > 0 && grid[row-1][col] == '1' && !visited.count({row-1, col})){
            dfs(row-1, col, grid);
        }
        // check right
        if(col < grid[0].size()-1 && grid[row][col+1] == '1' && !visited.count({row, col+1})){
            dfs(row, col+1, grid);
        }
        // check bottom
        if(row < grid.size()-1 && grid[row+1][col] == '1' && !visited.count({row+1, col})){
            dfs(row+1, col, grid);
        }
        // check left
        if(col > 0 && grid[row][col-1] == '1' && !visited.count({row, col-1})){
            dfs(row, col-1, grid);
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int island = 0;
        // loop through all the 1s
        for(int r =0; r < grid.size(); r++){
            for(int c = 0; c < grid[0].size(); c++){
                if(grid[r][c] == '1' && !visited.count({r,c})){
                    dfs(r, c, grid); // call it
                    island++;
                }
            }
        }
        return island;
    }
};