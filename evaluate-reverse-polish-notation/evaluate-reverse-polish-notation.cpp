class Solution {
public:
    int evalRPN(vector<string>& tokens) {


        stack<int> n; 

        for (string& t : tokens){
     
            if (!(t == "*" || t == "+" || t == "-" || t == "/")){
                n.push(stoi(t));
                continue; 
            }

            // Not a digit
            char op = t[0];
            int val = n.top();
            n.pop();

            switch(op){
                case('+'):
                    n.top() += val; 
                    break;
                case('-'):
                    n.top() -= val; 
                    break;
                case('*'):
                    n.top() *= val;
                    break;
                case('/'):
                    n.top() /= val;
                    break;
            }
        }

        return n.top();
    }   
        
         

};