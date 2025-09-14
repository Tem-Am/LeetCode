#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        // It is DP problem and it start from bottom to up

        int n = matrix.size();

        for(int row = n -2; row > -1; row--){
            for(int col = 0; col < n; col++ ){
                if(col == 0){
                    matrix[row][col] += min(matrix[row+1][col], matrix[row+1][col+1]);
                }
                else if (col == n-1){
                    matrix[row][col] += min(matrix[row+1][col], matrix[row+1][col-1]);
                }
                else{
                    int smallnum = min(matrix[row+1][col], matrix[row+1][col-1]);
                    matrix[row][col] += min(smallnum, matrix[row+1][col+1]);
                }
            }
        }

        return *min_element(matrix[0].begin(), matrix[0].end());
    }
};