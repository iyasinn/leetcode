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

        slow = slow->next; 
        while (slow){
            s.push(slow);
            slow = slow->next; 
        }

        while (!s.empty()){
            if (!head) cout << " hello no head here\n";
            else if (!head->next) cout << "No head next\n";
            if (!s.top()) cout << "no s.top that's valid\n";
            ListNode* temp = head->next; 
            head->next = s.top();
            head = head->next; 
            head->next = temp; 
            head = head->next; 
            s.pop();
        }
        head->next = nullptr; 
    }
};









