#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Make sure that left/first one is smaller one
        //  If nums1 has more number, we will switch nums1 and nums2
        if(nums1.size() > nums2.size()){
            vector<int> temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }

        // m and n are size of arrays
        int m = nums1.size();
        int n = nums2.size();

        // total is total number, and half is median index of total numner
        int total = m + n;
        int half = total / 2;

        // If total num is 0, return 0 
        // If total num is 1, return that number
        if(total == 0){
            return 0;
        }
        else if( total == 1){
            // Nums2 is almost bigger one
            return nums2[0];
        }
        // Starting index of each arrays if they are combined.
        float left = 0;
        float right = m;
        float nums1left = 0;
        float nums1right = 0;
        float nums2left = 0;
        float nums2right = 0;

        while(true){
            // Left is 0 and right is m initially, i -> m/2
            // j -> (m+n)/2 - (m)/2 -> n/2 initially
            int i = (left + right )/2; // Partition one
            int j = half - i; // Partition two

            if( i > 0){
                nums1left = nums1[i-1];
            }
            else{
                nums1left = -99999999;
            }

            if( i< m ){
                nums1right = nums1[i];
            }
            else{
                nums1right = 99999999;
            }

            if ( j > 0){
                nums2left = nums2[j-1];
            }
            else{
                nums2left = -999999999;
            }
            
            if(j < n){
                nums2right = nums2[j];
            }
            else{
                nums2right = 99999999;
            }

            if(nums1left <= nums2right && nums2left <= nums1right){
                if(total % 2 == 0){
                    float ans = (max(nums1left, nums2left) + min(nums1right, nums2right)) / 2;
                    cout << ans;
                    return ans;
                }
                else{
                    return min(nums1right, nums2right);
                }
            }
            else if (nums1left > nums2right){
                right = i - 1;
            }         
            else{
                left = i + 1;
            }
        }
    }
};