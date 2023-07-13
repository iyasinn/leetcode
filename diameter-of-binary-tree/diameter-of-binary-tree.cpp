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

 // Number of edges between two paths


class Solution {
public:

    int getHeight(TreeNode* root){
        if (!root){
            return 0; 
        }
        return 1 + max(getHeight(root->left), getHeight(root->right));
    }

    int diameterOfBinaryTree(TreeNode* root) {
        if (!root) {
            return 0; 
        }

        int left = getHeight(root->left);
        int right = getHeight(root->right);
        return max(left + right, max(diameterOfBinaryTree(root->left), diameterOfBinaryTree(root->right)));
    }
};