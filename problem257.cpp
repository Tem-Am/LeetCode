/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#include <vector>
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

    vector<string> paths; // all possible paths
    
    // backtrack functions
    void backtrack(string path, TreeNode* node){
        if( node == nullptr){
            return; // return if there is no more node
        }        
        
        if(path.length() == 0){
            path += to_string(node -> val);
        }
        else{
            path += "->" + to_string(node -> val);
        }
        
        // if there is no left and right, it measn that it is end
        if(node -> left == nullptr && node -> right == nullptr){
            paths.push_back(path);
        }

        backtrack(path, node -> left); // call all left side
        backtrack(path, node -> right); // call all right side after

    }

    vector<string> binaryTreePaths(TreeNode* root) {
        // base case
        if(root -> left == nullptr && root -> right == nullptr){
            return {to_string(root -> val)};
        }
        
        backtrack("", root);
        cout << paths[0];
        return paths;
    }
};