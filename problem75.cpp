#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        // every step i can swap or find the elements
        int red = 0; // 0s
        int white = 0; // 1s
        int blue = 0;  // 2s
        for(int num : nums){
            if(num == 0){
                red++;
            }
            else if(num == 1){
                white++;
            }
            else{
                blue++;
            }
        }
        white += red;
        blue += white;
        for(int i = 0; i < nums.size(); i++){
            if(i < red){
                nums[i] = 0;
            }
            else if(i < white){
                nums[i] = 1;
            }
            else{
                nums[i] = 2;
            }
        }
    }
};