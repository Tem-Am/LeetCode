#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    vector<vector<int>> comb;
    vector<int> current;
    void backtrack(int index, int num, int k)
    {
        if (current.size() == k)
        {
            comb.push_back(current);
            return;
        }

        for (int i = index; i <= num; i++)
        {
            current.push_back(i);
            backtrack(i + 1, num, k);
            current.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k)
    {
        current.clear();
        comb.clear();
        backtrack(1, n, k);
        return comb;
    }
};