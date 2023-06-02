class Solution {
public:
    // bool isValid(string s) {

    //     unordered_map<char, char> dict = {{')', '('}, {']', '['}, {'}', '{'}};
    //     stack<char> word; 
    //     for (auto c : s){
    //         if (c == '(' || c == '[' || c == '{') word.push(c);
    //         else if (dict.count(c)){
    //             if (word.empty() || dict[c] != word.top()) return false; 
    //             word.pop(); 
    //         }
    //     }
    //     return word.empty();
    // }


    // bool isValid(string s) {

    //     stack<char> word; 

    //     for (auto c : s){
    //         if (c == '(' || c == '[' || c == '{'){
    //             word.push(c);
    //         }
    //         if (c == '}' || c == ']' || c == ')'){
    //             if (word.empty() 
    //                 || (c == ')' && word.top() != '(')
    //                 || (c == ']' && word.top() != '[')
    //                 || (c == '}' && word.top() != '{')){
    //                     return false;
    //             }

    //             word.pop();
    //         }
    //     }
        
    //     return word.empty();
    // }

    bool isValid(string s) {

        stack<char> word; 

        for (auto c : s){

            if (c == '(' || c == '[' || c == '{'){
                word.push(c);
            }
            // Need else because code would run even if the above statement is true. 
            // Remember why we nee else
            else{
                if (word.empty() 
                    || (word.top() == '(' && c != ')')
                    || (word.top() == '[' && c != ']')
                    || (word.top() == '{' && c != '}')){
                        return false;
                }
                word.pop();
            }
            
        }
        return word.empty();
    }
        
        


    // bool isValid(string s) {
    //     stack<char> st; 
    //     for(auto i:s) {
    //         if(i=='(' or i=='{' or i=='[') st.push(i);  
    //         else {
    //             if(st.empty() or (st.top()=='(' and i!=')') or (st.top()=='{' and i!='}') or (st.top()=='[' and i!=']')) 
    //             return false;
    //             st.pop();  
    //         }
    //     }
    //     return st.empty(); 
    // }


};