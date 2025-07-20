#include <vector>
using namespace std;

class Solution
{
public:
    bool canJump(vector<int> &nums)
    {
        if (nums.size() == 1)
        {
            return true;
        }
        if (nums[0] == 0)
        {
            return false;
        }
        // the farthest jump that i can go from the current index
        int farjump = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            // this means that i stuck. so there is no possible way to get there
            if (i > farjump)
            {
                return false;
            }
            farjump = max(farjump, i + nums[i]);
        }
        return true;
    }
};