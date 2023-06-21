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
    // ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

    //     if (!list1 || !list2) return (list1) ? list1 : list2;
        
    //     if (list1->val > list2->val) swap(list1, list2);
    //     ListNode* head = list1; 

    //     while (list1 && list2){
    //         // list1 is always smaller
    //         if (!list1->next || list1->next->val > list2->val){
    //             ListNode* next = list1->next; 
    //             list1->next = list2; 
    //             list1 = next; 
    //             swap(list1, list2);
    //         }
    //         else{
    //             list1 = list1->next; 
    //         }
    //     }


    //     return head; 
    // }


    // Dummy node solution
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        if (!list1 || !list2) return (list1) ? list1 : list2;
        ListNode* ans = new ListNode(); 
        ListNode* curr = ans; 

        while (list1 && list2){
            if (list1->val < list2->val){
                curr->next = list1; 
                list1 = list1->next; 
            }
            else{
                curr->next = list2;
                list2 = list2->next; 
            } 
            curr = curr->next; 
        }

        if (list1) curr->next = list1; 
        else curr->next = list2; 
        return ans->next; 
    }


};