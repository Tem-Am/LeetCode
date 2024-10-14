#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max = 0;
        int start =1;
        int temp =0;
        int rep = 0;
        for(int i = 0; i< s.size(); i++){
            int ans = 1;
            if(rep == 0){
                for(int j =temp; j<i; j++){
                    if(s[j] != s[i]){
                        ans++;
                        cout << s[ans];
                    }
                    if(s[j] == s[i]){
                        rep++;
                        start = j+1;
                        j = i;
                    } 
                }       
            }
            if( rep > 0){
                temp = start;
                rep = 0;
            }
            cout << endl;
            if(ans > max){
                max = ans;
            }
        }
    return max;
    }
};

int main(){
    Solution a;
    int ans = a.lengthOfLongestSubstring("absa");
    cout << ans;
    return 0;
}