#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // Base case, when there is only one number
        if(nums.size() == 1){
            return nums[0];
        }

        // Dynamic programming --> check on every indexs
        int sum = 0;
        int largest = -99999;
        for(int i = 0; i<nums.size(); i++){
            sum += nums[i]; // add all elements
            if(sum < nums[i]){
                sum = nums[i]; // if sum is less, it is obvious
            }

            if(sum >= largest){
                largest = sum; // the large number
            }
        }
        return largest;
    }
};