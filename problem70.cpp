class Solution {
public:
    int climbStairs(int n) {
        // Base cases
        if(n == 1){
            return 1;
        }
        if(n == 2){
            return 2;
        }

        long oneStep = 2;
        long twoStep = 1;
        for(int i =2; i <= n; i++){
            long current = oneStep + twoStep;
            twoStep = oneStep;
            oneStep = current;
        }
        return twoStep;
    }
};