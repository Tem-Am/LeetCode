#include <vector>
#include <queue>
#include <algorithm>
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> answer;
        bool left_right = true; // check if we reverse it ot not
        // check if tree is not empty or no
        if(!root){
            return answer;
        }
        else{
            queue<TreeNode*> q;
            q.push(root);
            while(!q.empty()){
                int level_size = q.size();
                vector<int> values;
                for(int i = 0; i < level_size; i++){
                    TreeNode* node = q.front(); // pop it from the top
                    q.pop();
                    values.push_back( node -> val);

                    if(node -> left){
                        q.push(node->left);
                    }
                    if(node -> right){
                        q.push(node -> right);
                    }
                }

                if(!left_right){
                    reverse(values.begin(), values.end());
                }
                answer.push_back(values);
                left_right = !left_right;
            }
        }
        return answer;
    }
};