#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        // sorted --> add all intervals before newInterval 
        int i = 0; // index of intervals
        int len = intervals.size();
        vector<vector<int>> answer;

        // add all intervals before reaching newinterval starting point
        while(i < len && newInterval[0] > intervals[i][1]){
            answer.push_back(intervals[i]);
            i++;
        }

        // Now expand interval where overlap with newinterval
        while(i < len && intervals[i][0] <= newInterval[1]){
            newInterval[0] = min(intervals[i][0], newInterval[0]);
            newInterval[1] = max(intervals[i][1], newInterval[1]);
            i++;
        }
        answer.push_back(newInterval);

        // Now add remaining intervals

        while(i < len){
            answer.push_back(intervals[i]);
            i++;
        }

        return answer;
    }
};