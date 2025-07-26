#include <vector>
#include <iostream>
#include <map>
using namespace std;

class Solution
{
public:
    vector<string> message; // all possible message
    string current;         // current possible message
    map<char, string> phone = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}};

    void backtrack(int index, const string &digits)
    {
        if (current.length() == digits.length())
        {
            message.push_back(current);
            return;
        }
        for (char l : phone[digits[index]])
        {
            current.push_back(l);
            backtrack(index + 1, digits);
            current.pop_back();
        }
    };

    vector<string> letterCombinations(string digits)
    {
        // says all possible letter comb means that it is back track
        // numbers whichs includes letters
        if (digits.size() == 0)
            return {};
        backtrack(0, digits);
        return message;
    };
};