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
class Solution {
public:

    void dfs(TreeNode* root, priority_queue<int, vector<int>, greater<int>>& pq){
        if (!root){
            return; 
        }
        pq.push(root->val);
        dfs(root->left, pq);
        dfs(root->right, pq);
    }

    int kthSmallest(TreeNode* root, int k) {
        priority_queue<int, vector<int>, greater<int>> pq;
        dfs(root, pq);

        while (k > 1){
            pq.pop();
            k--;
        }

        return pq.top();
    }
};