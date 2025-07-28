#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Base case
        if(strs.size() == 0){
            return {{}};
        }

        // hashmap for all words
        unordered_map<string, vector<string>> anagrams;

        for(string s : strs){
            string temp = s; // save word before sort
            sort(s.begin(), s.end()); // sort the word
            anagrams[s].push_back(temp); // push word to it
        }
        vector<vector<string>> result;

        for (auto& pair : anagrams) {
            result.push_back(pair.second);
        }
        return result;
    }
};