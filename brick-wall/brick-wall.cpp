class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        
        unordered_map<int, int> m;

        for (auto& row : wall){
            int edge = 0; 
            for (int i = 0; i < row.size() - 1; i++){
                edge += row[i];
                m[edge]++;
            }
        }

        int maxCount = 0; 
        for (auto [key, val] : m){
            maxCount = max(maxCount, val);
        }

        return wall.size() - maxCount; 




    }
};