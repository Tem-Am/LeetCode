#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    void rotate(vector<vector<int>> &matrix)
    {

        // Step 1: Transpose the matrix
        for (int i = 0; i < matrix.size(); i++)
        {
            for (int j = i + 1; j < matrix.size(); j++)
            {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // Step 2: reverse row
        // Step 2: Reverse each row
        for (int i = 0; i < matrix.size(); ++i)
        {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};