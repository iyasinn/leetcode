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

    // Unordered Set method
    // O(n) complexity
    // bool hasCycle(ListNode *head) {
    //     unordered_set<ListNode*> visited;
    //     ListNode* curr = head; 

    //     while (curr){
    //         if (visited.find(curr) != visited.end()) return true; 
    //         visited.insert(curr);
    //         curr = curr->next; 
    //     }
    //     return false; 
    // }

    // Maybe two pointer
    // bool hasCycle(ListNode *head) {
    //     if (!head) return false;
        
    //     ListNode* curr = head; 
    //     ListNode* curr1 = head->next;

    //     while (curr && curr1){
    //         if (curr == curr1) return true; 
    //         curr = curr->next; 
    //         curr1 = curr1->next; 
    //         curr1 = curr1 ? curr1->next : curr1;
    //     }
    //     return false; 
    // }


    // Improved solution
    // O(n)
    bool hasCycle(ListNode *head) {
        if (!head) return false;
        
        ListNode* curr = head; 
        ListNode* curr1 = head->next;

        while (curr1 && curr1->next){
            if (curr == curr1) return true; 
            curr = curr->next; 
            curr1 = curr1->next->next;
        }
        return false; 
    }

};