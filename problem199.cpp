#include <vector>
#include <queue>
#include <iostream>
using namespace std;
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        // answer vector
        vector<int> asnwer;
        queue<TreeNode*> q;
        // Check if root is empty or not
        if(!root){
            return {};
        }
        else{
            q.push(root); // initial value
            while(!q.empty()){
                int totalnodes = q.size();
                TreeNode* last;
                for(int i = 0; i < totalnodes; i++){
                    TreeNode* node = q.front(); // get the fist element in queue
                    if(i == totalnodes - 1){
                        last = node;
                    }
                    q.pop(); // pop that element 
                    if( node -> left){
                        q.push(node -> left);
                    }
                    if( node -> right ){
                        q.push(node -> right);
                    }
                }
                asnwer.push_back(last -> val);
            }
        }
        return asnwer;
    }
};