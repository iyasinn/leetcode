

class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        auto valid = [&](int days){
            int count = 0; 
            int rolling = 0; 
            for (int i = 0; i < bloomDay.size(); i++){
                if (bloomDay[i] <= days) { rolling += 1; } 
                else { rolling = 0; }
                if (rolling == k){ count += 1; rolling = 0; }
            }
            return count >= m; 
        };
        int l = 0, r = 1e9 + 1; 
        int solution = -1; 

        while (l < r){
            int mid = l + ((r - l) / 2);
            if (valid(mid)) { 
                r = mid; 
                solution = r;  
            }
            else { l = mid + 1; }
        }
        return solution; 
    }
};