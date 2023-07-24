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

 // Put all elements into a min heap to get the kth smallest element
 // Put all elements into a vector and then sort 
 // COunting sort not good cuz no frequency  here
 // Prioritie queues are usually best for the kth smallest element
 // In order traversal of a Binary Search Tree will ALWAYS give you a sorted array 
class Solution {
public:

    void dfs(TreeNode* root, vector<int>& arr){
        if (!root){
            return; 
        }
        dfs(root->left, arr);
        arr.push_back(root->val);
        dfs(root->right, arr);
    }

    int kthSmallest(TreeNode* root, int k) {
        vector<int> arr; 
        dfs(root, arr);
        return arr[k - 1];
    }
};