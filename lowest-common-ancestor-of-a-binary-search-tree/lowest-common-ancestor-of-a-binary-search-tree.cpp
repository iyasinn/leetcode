/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // We're dealing with a bst 
        if (!root || !p || !q){
            return nullptr; 
        }

        // split has occured
        if ((root->val >= p->val && root->val <= q->val) || (root->val >= q->val && root->val <= p->val)){
            return root; 
        }

        // Else we simply check both sides of the tree, though only one side is needed
        if (root->val > p->val){
            return lowestCommonAncestor(root->left, p, q);
        }
        else{
            return lowestCommonAncestor(root->right, p, q);
        }
    }
};