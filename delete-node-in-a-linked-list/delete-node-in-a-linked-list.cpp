/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {


        if (!node){ return; }
        
        ListNode* temp = node->next->next;
        node->val = node->next->val;
        delete node->next; 
        node->next = temp; 
    }



};