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
    It helps to know the GCD algorithm 
    I need to understand why this algorithm works 
 */


int getGCD(int a, int b){
    if (b == 0){
        return a;
    }
    return getGCD(b, a % b);
}

class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {

        auto start = head; 

        while (head && head->next){

            auto second = head->next; 

            auto temp = new ListNode(getGCD(head->val, head->next->val)); 

            head->next = temp; 
            temp->next = second; 
            head = second; 
        }

        return start; 
    }
};