#include <vector>
#include <queue>
#include <iostream>
using namespace std;

class Solution
{
public:
    bool canReach(vector<int> &arr, int start)
    {
        // Base case
        if (arr[start] == 0)
        {
            return true;
        }

        // Have a queue to check everything
        queue<int> jumpque;
        jumpque.push(start); // the first element

        while (!jumpque.empty())
        {
            int currentIndex = jumpque.front();
            jumpque.pop();
            if (arr[currentIndex] == 0)
            {
                return true;
            }
            int jump = arr[currentIndex]; // marking the known position
            arr[currentIndex] = -1;       // mark this as known
            int left = currentIndex - jump;
            int right = currentIndex + jump;
            if (0 <= left && arr[left] != -1)
            {
                jumpque.push(left);
            }

            if (right < arr.size() && arr[right] != -1)
            {
                jumpque.push(right);
            }
        }
        return false;
    }
};