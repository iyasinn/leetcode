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

    // void rec(vector<int>& v, TreeNode* root){
    //     if (!root) return;
    //     rec(v, root->left);
    //     v.push_back(root->val);
    //     rec(v, root->right);
    // }

    // vector<int> inorderTraversal(TreeNode* root) {
    //     vector<int> sol;
    //     rec(sol, root);
    //     return sol;
    // }


    vector<int>v;
    vector<int> inorderTraversal(TreeNode* root) {
        if(root==NULL)return v;
        inorderTraversal(root->left);
        v.push_back(root->val);
        inorderTraversal(root->right);
        return v;
    }
};