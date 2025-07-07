#include <map>
#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        // Stack for opening brackets
        stack<int> openStack;

        // Map for mapping each opening brackets to closing brackets
        map<char, char> bracket;
        bracket['('] = ')';
        bracket['{'] = '}';
        bracket['['] = ']';
        // Loop throug all the char in s 
        for(int i = 0; i < s.length(); i++){
            // If it is opening brackets, add to stack
            if(bracket.count(s[i])){
                openStack.push(s[i]);
            }
            // If it is closing bracket, compare with opening bracket from the stack
            else if(s[i] == ')'){
                if(openStack.empty()){
                    return false;
                }
                char open = openStack.top();
                if(bracket[open] != s[i]){
                    return false;
                }
                openStack.pop();
            }
            else if(s[i] == '}'){
                if(openStack.empty()){
                    return false;
                }
                char open = openStack.top();
                if(bracket[open] != s[i]){
                    return false;
                }
                openStack.pop();
            }
            else if(s[i] == ']'){
                if(openStack.empty()){
                    return false;
                }
                char open = openStack.top();
                if(bracket[open] != s[i]){
                    return false;
                }
                openStack.pop();
            }
        }
        if(openStack.empty()){
            return true;
        }
        else{
            return false;
        }
    }
};