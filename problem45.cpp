#include <vector>
using namespace std;

class Solution
{
public:
    int jump(vector<int> &nums)
    {
        int steps = 0;   // track the lowest step
        int farjump = 0; // farthest i can jump the current index
        int end = 0;     // this the end farthest at current step

        for (int i = 0; i < nums.size() - 1; i++)
        {
            farjump = max(farjump, i + nums[i]);

            if (end == i)
            {
                steps++;
                end = farjump;
            }
        }
        return steps;
    }
};