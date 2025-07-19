#include <iostream>
using namespace std;
class Solution
{
public:
    int numDecodings(string s)
    {
        // Base case where no need to run code
        if (s.length() == 1)
        {
            if (s[0] != '0')
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }
        // 03123... is not possible to decode because of leading 0
        if (s.length() > 1 && s[0] == '0')
        {
            return 0;
        }
        // Before adding next letter, it is current possible combination
        int current = 1;
        // After adding letter, if letter is between 10 and 26, we need to also add previous one
        int prev = 1;

        for (int i = 1; i < s.length(); i++)
        {
            int num = s[i] - '0';
            int num2 = stoi(s.substr(i - 1, 2));
            int next = 0;
            // So, it is not a zero
            if (num != 0)
            {
                next += current;
            }
            if (9 < num2 && num2 < 27)
            {
                next += prev;
            }
            // Update current and prev
            if (num == 0)
            {
                if (num2 > 26)
                {
                    return 0;
                }
                else
                {
                    current = next;
                }
            }
            else
            {
                prev = current;
                current = next;
            }
        }
        return current;
    }
};