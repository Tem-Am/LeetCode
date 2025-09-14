#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        // DP problem 
        // Base case 
        if(triangle.size() == 1){
            return triangle[0][0];
        }

        // Goes from bottom to top
        // Update number from bottom row, and choose the min number from the option

        for(int row = triangle.size()-1; row > 0; row--){
            // Goes through all number in current row
            for(int index = 0; index < triangle[row].size()-1; index++){
                // Update the next row
                triangle[row-1][index] += min(triangle[row][index], triangle[row][index+1]);
            }
        }
        return triangle[0][0];
    }
};