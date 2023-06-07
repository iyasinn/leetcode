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
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root){
            return 0; 
        }
        if (!root->left && !root->right){
            return 1; 
        }

        int x = numeric_limits<int>::max(); 
        x = (root->left) ? min(x, 1 + minDepth(root->left)) : x;
        x = (root->right) ? min(x, 1 + minDepth(root->right)) : x; 

        return x;  
    }
};