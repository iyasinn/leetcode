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
        /*
            if (!head) return;

            create mapping
            create tempHead;
            mapping.insert(null -> null) 

            create walkTemp
            create walkHead

            while (walkHead) 
                our temphead next will point to a new list with the same value as walk head
                we will map our walkHead to that new walkTemp

            waslkTemp back = to tempHead->next
            walkHead = head

            while (walkHead)
                waslkTemp->random = hashmap(walkHead->next)
        
        */

        if (!head) { return nullptr; }

        unordered_map<Node*, Node*> rel;

        // dummy head
        Node* sol = new Node(0);
        Node* walkSol = sol;
        Node* walkHead = head; 

        while (walkHead){
            walkSol->next = new Node(walkHead->val);
            rel[walkHead] = walkSol->next;
            walkSol = walkSol->next;
            walkHead = walkHead->next;
        }

        rel[nullptr] = rel[nullptr];

        walkSol = sol->next;
        walkHead = head;

        while (walkHead){
            walkSol->random = rel[walkHead->random];
            walkSol = walkSol->next;
            walkHead = walkHead->next;
        }

        return sol->next;
    }
};

















