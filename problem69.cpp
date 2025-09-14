#include <iostream>
using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        // Binary search
        // Base Case

        if(x < 2){
            return x;
        } 

        long left = 1;
        long right = x/2;

        while( left <= right){
            long mid = (left + right) / 2;
            long sqr = mid * mid;

            if(sqr == x){
                return mid;
            }
            else if(sqr > x){
                right = mid -1;
            }
            else{
                left = mid + 1;
            }
        }
        return right;
    }    
};