
class Solution {
public:

    struct Cont {
        int open = 0; 
        string s = "";
    };

    vector<string> generateParenthesis(int n) {

        vector<string> sols;

        stack<Cont> bfs; 
        bfs.push({1, "("});

        while (!bfs.empty()){

            Cont top = bfs.top();
            cout << top.s << endl;
            bfs.pop();

            if (top.s.size() != n * 2){

                top.s.push_back('(');
                bfs.push({top.open + 1, top.s});
                top.s.pop_back();
                top.s.push_back(')');
                if (top.open > 0){
                    bfs.push({top.open - 1, top.s});
                    top.s.pop_back();
                }
            }
            else if (top.open == 0){
                sols.push_back(top.s);
            }
        }

        return sols; 
    }
};
