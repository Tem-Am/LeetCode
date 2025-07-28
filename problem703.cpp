#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target) {
        // Binaray search
        int left = 0;
        int right = nums.size()-1;

        while(left <= right){
            // find the midpoint
            int mid = left + (right - left)/2;
            if(nums[mid] == target){
                return mid;
            }
            else if(nums[mid] > target){
                right = mid -1 ; //  check the left side
            }
            else{
                left = mid + 1; // this is the right side
            }
        }
        return -1; 
    }
};