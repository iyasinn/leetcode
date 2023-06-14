class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temp) {
        vector<int> sols(temp.size(), 0);
        stack<int> t; 
        for (int i = 0; i < temp.size(); i++){
            while (!t.empty() && temp[i] > temp[t.top()]){
                sols[t.top()] = i - t.top(); 
                t.pop();
            }
            t.push(i);
        }
        return sols;
    }
};