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

/*
we need to simply validate that the tree is correct
Currently we have 2
then we have 1 
and we know that 1 can never exceed 2
Then we go to the left of 1, and the max changes to 1
If we go to the right of 1, then the min is 1, but the max is still 2
So we can essentially have a max and min
At the beginning there is no specific max and min 
*/


class Solution {
public:

    bool dfs(TreeNode* root, long long min, long long max){
        if (!root){
            return true; 
        }
        if (root->val <= min || root->val >= max){
            cout << "lol"<< endl;
            return false; 
        }
        return dfs(root->left, min, root->val) && dfs(root->right, root->val, max);
    }

    bool isValidBST(TreeNode* root) {
        return dfs(root, numeric_limits<long long>::min(), numeric_limits<long long>::max());
    }
};