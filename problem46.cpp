#include <vector>
#include <unordered_set>
#include <iostream>
using namespace std;
class Solution
{
public:
    vector<vector<int>> permutation;
    vector<int> current;
    unordered_set<int> used;
    void backtrack(vector<int> &nums)
    {
        // if the path has all element push to permutation
        if (current.size() == nums.size())
        {
            permutation.push_back(current); // the current path
            return;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            if (used.contains(nums[i]))
            {
                continue;
            }
            used.insert(nums[i]);       // add to used set
            current.push_back(nums[i]); // add to current combination
            backtrack(nums);            // call it again
            used.erase(nums[i]);
            current.pop_back();
        }
    }

    vector<vector<int>> permute(vector<int> &nums)
    {
        permutation.clear();
        current.clear();
        backtrack(nums);
        return permutation;
    }
};