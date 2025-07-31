#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // hash table for indexs and target - nums[index]
        unordered_map <int, int> indexs;

        for(int i = 0; i < nums.size(); i++){
            // key -> target-num
            indexs[target-nums[i]] = i;
        }
        // loop again to get nums if targer-nums in dic
        // return index and dic value? only they are different
        for(int i = 0; i< nums.size(); i++){
            if(indexs.count(nums[i])){ // this means this number other exist!
                if(i != indexs[nums[i]]){
                    return {i, indexs[nums[i]]};
                }
            }
        }
        return {};
    }
};