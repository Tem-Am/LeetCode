#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        // Size of list
        int len = nums.size();
        vector<int> answer;
        int prefix = 1;
        for (int i = 0; i < len; i++)
        {
            if (i == 0)
            {
                answer.push_back(1);
            }
            else
            {
                prefix *= nums[i - 1];
                answer.push_back(prefix);
            }
        }
        int suf = 1;
        for (int j = len - 1; j > -1; j--)
        {
            answer[j] *= suf;
            suf *= nums[j];
        }

        return answer;
    }
};