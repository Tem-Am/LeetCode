#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        // Case where no need to do any other steps
        int k = 0;
        for(int num : nums){
            if(num != val){
                nums[k] = num;
                k++;
            }
        }
        return k;
    }
};