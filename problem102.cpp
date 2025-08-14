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
    vector<vector<int>> levelOrder(TreeNode* root) {
        // Write queue and ans vector
        queue<TreeNode*> q;
        vector<vector<int>> ans;
        if(!root){
            return ans; // base case 
        }
        q.push(root); // add the first node as root
        while(!q.empty()){
            int length = q.size();
            vector<int> node_vals;
            for(int i = 0;  i< length; i++){
                TreeNode* node = q.front();
                node_vals.push_back(node -> val);
                q.pop();
                if(node -> left){
                    q.push(node -> left);
                }
                if(node -> right){
                    q.push(node -> right);
                }
            }
            ans.push_back(node_vals);
        }
        return ans;
    }
};