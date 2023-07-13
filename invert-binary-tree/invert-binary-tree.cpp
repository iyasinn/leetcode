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
What happens if empty? Return same thing
The ordering entirely has to switch, so we are essentially reflecting it across the vertical axis
So we can map this to a recursive problem, potentially tree recursive 
We know that for each element, its two children will be reverse, so we dont need to have
a helper function 
Check the sub problem
Assuming 2 is moved fine, we see 1 and 3 flip regardless, ignoring what happens to 2

So we can recursively solve this probem
*/

class Solution {
public:
    // Not a recursive problem
    // O(n) complexity for each root
    // O(n) space on the stack, because we are doing a dfs to flip each subtree 
    // And this is not tail recursive
    TreeNode* invertTree(TreeNode* root) {
        if (!root){ return nullptr; }
        // swaps the address stored at root->left and root->right
        swap(root->left, root->right);
        invertTree(root->left);
        invertTree(root->right);
        return root; 
    }
};