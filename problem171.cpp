#include <iostream>
#include <string>
#include <stack>
#include <vector>
using namespace std;

class Solution
{
public:
    string simplifyPath(string path)
    {
        // Base case
        if (path.length() == 1)
        {
            return "/";
        }
        // Can be dynamic programming
        // all slashes are like a dot, which saying the path
        stack<string> s; // all paths
        string p = "";   // for name or operations with cd
        for (int i = 1; i < path.length(); i++)
        {
            if (path[i] != '/')
            {
                p += path[i]; // create
            }
            else
            { // it is slash
                if (p.length() != 0)
                {
                    s.push(p);
                    p = "";
                }
            }
        }
        if (p.length() != 0)
        { // if ending index is not slash, we did not add last string
            s.push(p);
        }
        stack<string> newpath;
        int pop = 0;
        while (!s.empty())
        {
            string rule = s.top(); // to not call top many times
            if (rule == ".")
            {
                s.pop(); // just pop, no need to anything;
            }
            else if (rule == "..")
            {
                s.pop();
                if (!s.empty())
                {
                    pop++; // if not empty, pop it again;
                }
            }
            else
            {
                if (pop == 0)
                {
                    newpath.push(rule);
                    s.pop();
                    newpath.push("/");
                }
                else
                {
                    s.pop();
                    pop--;
                }
            }
        }
        path = "";
        while (!newpath.empty())
        {
            path += newpath.top();
            newpath.pop();
        }
        if (path.length() == 0)
        {
            return "/";
        }
        return path;
    }

    string simplifyPath2(string path)
    {
        vector<string> stack;
        stringstream ss(path);
        string token;

        while (getline(ss, token, '/'))
        {
            if (token == "" || token == ".")
                continue;
            if (token == "..")
            {
                if (!stack.empty())
                    stack.pop_back();
            }
            else
            {
                stack.push_back(token);
            }
        }

        if (stack.empty())
            return "/";

        string result;
        for (const string &dir : stack)
        {
            result += "/" + dir;
        }

        return result;
    }
};