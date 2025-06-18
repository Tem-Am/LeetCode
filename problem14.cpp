#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty()){
            return "";
        }
        if(strs.size() == 1){
            return strs[0];
        }
        string first_letter = strs[0];
        string answer = "";
        int index = 0;
        while(index < first_letter.length()){
            for(int i =1; i<strs.size(); i++){
                if(first_letter[index] != strs[i][index]){
                    return(first_letter.substr(0, index));
                }
            }
            index++;
        }
        return first_letter;
    }
};