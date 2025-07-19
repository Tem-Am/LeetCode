#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std;
class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        unordered_set<int> num_set;
        for (int i = 0; i < nums.size(); i++)
        {
            num_set.insert(nums[i]);
        }
        int longest_seq = 0;
        for (int num : num_set)
        {
            if (num_set.contains(num - 1) == false)
            {
                int start_num = num + 1;
                int sequence = 1;
                while (num_set.contains(start_num))
                {
                    sequence++;
                    start_num++;
                }
                if (sequence > longest_seq)
                {
                    longest_seq = sequence;
                }
            }
        }
        return longest_seq;
    }
};