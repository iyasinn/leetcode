/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:

    ListNode* reverseList(ListNode* head){
        ListNode* prev = nullptr; 
        while (head){
            ListNode* temp = head->next; 
            head->next = prev; 
            prev = head; 
            head = temp; 
        }
        return prev; 
    }

    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (!head) return nullptr; 

        head = reverseList(head);
        ListNode* dummy = new ListNode(1000); 
        dummy->next = head; 
        ListNode* sol = dummy;

        n -= 1; 
        while (n > 0){
            sol = sol->next;
            n--;
        }

        ListNode* temp = sol->next->next; 
        sol->next = temp; 

        head = dummy->next; 
        head = reverseList(head);
        delete dummy;
        return head; 

    }
};