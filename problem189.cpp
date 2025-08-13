#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size(); // size of n
        // if k is greater than size of nums, we need remainder of n / k
        k =  k % n; // new k
        // Base case
        if(k == 0){
            return;
        }

        int count = 0; // number of elements are changed
        for(int i =0; i < n; i++){
            int current = i; // this is starting point 
            int prev = nums[current]; // this is the number will be changed 
            if(count >= n){
                break;
            }
            bool run = true;
            while(run){
                int nextIndex = (current + k) % n; // next index
                int save = nums[nextIndex]; // save next index number
                nums[nextIndex] = prev; // nextindex will have prev number 
                prev = save; // prev number will be updated to next number
                current = nextIndex; // also current index will be updated too.
                count++; // number of changed element in array will be increasd by one
                if(current == i){
                    run = false;
                }
            }   
        }
    }
};