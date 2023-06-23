class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        
        unordered_map<int, int> m;
        int maxCount = 0; 

        for (auto& row : wall){
            int edge = 0; 
            for (int i = 0; i < row.size() - 1; i++){
                edge += row[i];
                m[edge]++;
                maxCount = max(maxCount, m[edge]);
            }
        }

        return wall.size() - maxCount; 
    }
};