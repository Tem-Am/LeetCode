#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> answer; // this includes all the answers
    vector<int> current;
    int total = 0;
    // this is backtrack algorithm
    void backtrack(int start, int target, vector<int>& candidates){
        if(total == target){
            answer.push_back(current); // if it is true, add it
            return; // return nothing
        }
        if(total >= target){
            return; // need to return back
        }

        for(int i = start; i < candidates.size(); i++){
            total += candidates[i];
            current.push_back(candidates[i]);
            backtrack(i, target, candidates);
            total -= current[current.size()-1];
            current.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        answer.clear();
        current.clear();
        backtrack(0, target, candidates);
        return answer;
    }
};