class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
    
        unordered_set<int> mp(nums.begin(), nums.end());
        int best = 0; 

        for (int& n : nums){
            if (mp.count(n - 1)){
                continue; 
            }
            int curr = 0; 
            while (mp.count(n)){
                n++; 
                curr++;
            }
            best = max(best, curr);
        }

        return best; 
    }
};