/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {

        if (!head) { return nullptr; }

        unordered_map<Node*, Node*> rel;
        rel[nullptr] = nullptr;

        Node* temp = head; 

        // Create all the new copies with a mapping
        while (temp){
            rel[temp] = new Node(temp->val);
            temp = temp->next;
        }

        temp = head;

        // Link the next and random values of the new copies
        while (temp){
            rel[temp]->next = rel[temp->next];
            rel[temp]->random = rel[temp->random];
            temp = temp->next;
        }

        return rel[head];
    }

};

















