#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    string nextWord(string s){
        // Basic variables for string
        string result = "";
        int count = 1;
        char currentD = s[0];
        for(int i = 1; i < s.size(); i++){
            if(currentD == s[i]){
                count++;
            }
            else{
                string strDigit = to_string(count);
                result += strDigit;
                result += currentD;

                count = 1;
                currentD = s[i];
            }
        }
        string strDigit = to_string(count);
        result += strDigit;
        result += currentD;
        return result;
    }


    string countAndSay(int n) {
        
        // Base Case
        if(n == 1){
            return "1";
        }

        // If n is greater then one, then current will be "1" by default
        string current = "1";

        for(int i = 2; i < n+1; i++){
            current = nextWord(current);
        }

        return current;
    }
};