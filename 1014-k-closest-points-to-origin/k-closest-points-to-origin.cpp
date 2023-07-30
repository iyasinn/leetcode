class Solution {
public: 
    // l < r means r is better 
    // so we want small to large
    static bool compare(vector<int>& l, vector<int>& r){
        return (l[0] * l[0]) + (l[1] * l[1]) < (r[0] * r[0]) + (r[1] * r[1]);
    }


    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        sort(points.begin(), points.end(), compare);
        vector<vector<int>> sol; 
        for (int i = 0; i < k; i++){
            sol.push_back({points[i][0], points[i][1]});
        }
        return sol; 
    }
};