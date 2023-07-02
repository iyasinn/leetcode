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
    // Node* copyRandomList(Node* head) {

    //     if (!head) { return nullptr; }

    //     unordered_map<Node*, Node*> rel;
    //     rel[nullptr] = nullptr;

    //     Node* temp = head; 

    //     // Create all the new copies with a mapping
    //     while (temp){
    //         rel[temp] = new Node(temp->val);
    //         temp = temp->next;
    //     }

    //     temp = head;

    //     // Link the next and random values of the new copies
    //     while (temp){
    //         rel[temp]->next = rel[temp->next];
    //         rel[temp]->random = rel[temp->random];
    //         temp = temp->next;
    //     }

    //     return rel[head];
    // }

    Node* copyRandomList(Node* head) {

        // This solution wont work because youc ant modify the original linked list, which is kind of obvious :(
        // Maybe we can unmodify if though
        if (!head) { return nullptr; }

        // Creating zigzag merged list
        // Unique method of merging a list
        for (Node* curr = head; curr != nullptr;){
            Node* temp = curr->next; 
            curr->next = new Node(curr->val);
            curr->next->next = temp;
            curr = temp; 
        }

        // Setting the randoms
        for (Node* curr = head; curr != nullptr;){
            Node* copy = curr->next; 
            copy->random = (curr->random) ? curr->random->next : nullptr; 
            curr = curr->next->next; 
        }

        Node* sol = head->next; 

        // // Fixing the next connections
        for (Node* curr = head; curr != nullptr;){
            Node* copy = curr->next; 
            curr->next = curr->next->next; 
            copy->next = (curr->next) ? curr->next->next : nullptr; 
            curr = curr->next; 
        }

        return sol;
    }


};

















