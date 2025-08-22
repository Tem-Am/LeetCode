#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 0;
        for(int num : nums){
            // Check k is less than two
            // if greater, check current num is not same as number two index before it
            if(k < 2 || num != nums[k-2]){
                nums[k] = num; 
                k++;
            }
        }
        return k;
    }
};