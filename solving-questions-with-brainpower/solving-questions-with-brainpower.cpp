class Solution {
public:
    // Simple recursive solution
    // long long mostPoints(vector<vector<int>>& q, int i=0) {
    //     if (i >= q.size()) { return 0; }
    //     return max(q[i][0] + mostPoints(q, i + q[i][1] + 1), mostPoints(q, i + 1));
    // }

    // top down
    // long long top(vector<vector<int>>& q, int i, vector<long long>& tab) {
    //     if (i >= q.size()) { return 0; }
    //     if (tab[i] != -1) return tab[i];
    //     return tab[i] = max(q[i][0] + top(q, i + q[i][1] + 1, tab), top(q, i + 1, tab));
    // }

    // long long mostPoints(vector<vector<int>>& q) {
    //     vector<long long> tab(q.size() + 1, -1);
    //     return top(q, 0, tab);
    // }

    // bottom up 
    // tab represents the last question you have to do and no other
    // long long mostPoints(vector<vector<int>>& q) {

    //     vector<long long> tab(q.size(), -1);
    //     tab[0] = q[0][0];

    //     for (int i = 1; i < q.size(); i++){

    //         long long most = 0; 

    //         for (int j = i - 1; j >= 0; j--){
    //             if (j + q[j][1] < i){
    //                 most = max(most, tab[j]);
    //             }
    //         }

    //         tab[i] = max(q[i][0] + most, tab[i - 1]);
    //     }

    //     return tab[q.size() - 1];
    // }

    // Bottom up that makes more sense
    long long mostPoints(vector<vector<int>>& q) {

        vector<long long> tab(q.size(), -1);
    
        for (int i = q.size() - 1; i >= 0; i--){
            tab[i] = q[i][0];
            if (i + q[i][1] + 1 < q.size()){
                tab[i] = max(tab[i], q[i][0] + tab[i + q[i][1] + 1]);
            }
            if (i + 1 < q.size()){ 
                tab[i] = max(tab[i], tab[i + 1]); 
            }
        }
        return tab[0];
    }


};