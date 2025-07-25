#include <vector>
#include <iostream>
using namespace std;
class Solution
{
public:
    vector<vector<int>> allsets; // this is answer
    vector<int> current;         // this current sets

    void backtrack(int start, vector<int> &nums)
    {
        allsets.push_back(current);

        for (int i = start; i < nums.size(); i++)
        {
            current.push_back(nums[i]);
            backtrack(i + 1, nums);
            current.pop_back();
        }
    }

    vector<vector<int>> subsets(vector<int> &nums)
    {
        allsets.clear();
        current.clear(); // make sure that they are empty;
        backtrack(0, nums);
        return allsets;
    }
};