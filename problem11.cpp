#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int max_container = 0;
        int temp = 0;
        while( left < right){
            if(height[left] <= height[right]){
                temp = height[left] * (right - left);
                left++;
            }
            else{
                temp = height[right] * (right - left);
                right--;
            }

            if(max_container < temp){
                max_container = temp;
            }
        }
        return max_container;
    }
};