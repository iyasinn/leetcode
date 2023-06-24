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
 
/*
U
We want the start and end of each segment to be next to each other
If we have an empty head, we return that head
If we have a head of size 1, we return it
If we have a head of size 2, we return it 
Recursive solution would rack up space
*/

class Solution {
public:
    void reorderList(ListNode* head) {

        if (!head || !head->next) return; 

        stack<ListNode*> s; 
        ListNode* slow = head; 
        ListNode* fast = head; 

        while (fast && fast->next && fast->next->next){
            slow = slow->next; 
            fast = fast->next->next; 
        }


        ListNode* temp = slow->next; 
        slow->next = nullptr; 
        slow = temp; 

        ListNode* prev = nullptr;
        while (slow){
            ListNode* temp = slow->next; 
            slow->next = prev; 
            prev = slow; 
            slow = temp; 
        }
        slow = prev; 


        while (slow){
            ListNode* t1 = head->next;
            ListNode* t2 = slow->next; 
            head->next = slow; 
            slow->next = t1; 
            head = t1; 
            slow = t2; 
        }
        // head->next = nullptr; 
    }
};









