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

    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> s; 
        int processed = 0; 
        s.push(root);
        while (!s.empty()){
            TreeNode* top = s.top();
            s.pop();
            if (top->left){
                s.push(top);
                s.push(top->left);
                top->left = nullptr; 
                continue; 
            }
            processed += 1; 
            if (processed == k){
                return top->val;
            }
            if (top->right){
                s.push(top->right);
            }

        }
        return 0;
    }
};