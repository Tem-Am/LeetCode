#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // Need to sort them first 
        // Then start with adding to asnwer
        // Base case
        if(intervals.size() == 1){
            return {{intervals[0][0], intervals[0][1]}};
        }
        // Sort them
        sort(intervals.begin(), intervals.end());

        int start = intervals[0][0]; // start point of  current interval
        int end = intervals[0][1]; // end point of current interval
        vector<vector<int>> answer;
        for(int i = 1; i < intervals.size(); i++){
            if(intervals[i][0] <= end){ // this means that interval exist in current 
                if(intervals[i][1] > end){
                    end = intervals[i][1]; // if inteval's end point is greater, change it
                }
            }
            else{
                answer.push_back({start, end});
                start = intervals[i][0]; // new values for end and start
                end = intervals[i][1];
            }
        }
        answer.push_back({start,end});
        return  answer;
    }  

};