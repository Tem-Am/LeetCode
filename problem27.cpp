#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        }

        int uniNum = 0;
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] != nums[uniNum]){
                uniNum++;
                nums[uniNum] = nums[i];
            }
        }
        return uniNum+1;
    }
};