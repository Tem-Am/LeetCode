#include <vector>
#include <unordered_set>
using namespace std;

class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        // Need a unordereds-set
        unordered_set<int> hashSet;
        for (int num : nums)
        {
            if (hashSet.count(num))
            {
                return true;
            }
            hashSet.insert(num);
        }
        return false;
    }
};