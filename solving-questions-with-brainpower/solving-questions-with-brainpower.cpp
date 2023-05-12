class Solution {
public:
    // Simple recursive solution
    // long long mostPoints(vector<vector<int>>& q, int i=0) {
    //     if (i >= q.size()) { return 0; }
    //     return max(q[i][0] + mostPoints(q, i + q[i][1] + 1), mostPoints(q, i + 1));
    // }

    // top down
    long long top(vector<vector<int>>& q, int i, vector<long long>& tab) {
        if (i >= q.size()) { return 0; }
        if (tab[i] != 0) return tab[i];

        return tab[i] = max(q[i][0] + top(q, i + q[i][1] + 1, tab), top(q, i + 1, tab));
    }

    long long mostPoints(vector<vector<int>>& q) {
        vector<long long> tab(q.size() + 1);
        return top(q, 0, tab);
    }
};