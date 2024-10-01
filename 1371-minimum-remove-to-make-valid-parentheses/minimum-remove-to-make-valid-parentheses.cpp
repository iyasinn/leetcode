/*

Brute force is try all possible removals to make valid

Greedy
If something breaks the pairing, then remove, else don't remove 
But that favors the open parentheses

( ( )
So two open, and close
We could try matching and see removal 

Worst case: We remove all of them



*/

class Solution {
public:
    string minRemoveToMakeValid(string s) {

        stack<int> st; 

        for (int i = 0; i < s.size(); i++){
            char c = s[i]; 

            if (c == '(') st.push(i); 
            else if (c == ')' && st.size() == 0){
                s[i] = '.'; 
            }
            else if (c == ')'){
                st.pop(); 
            }
        }

        while (st.size() > 0) { s[st.top()] = '.'; st.pop(); }

        std::string solution; 
        for (char c : s){
            if (c != '.') solution.push_back(c); 
        }

        return solution; 

        






    }
};