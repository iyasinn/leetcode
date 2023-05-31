class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        vector<vector<int>> res;
        set<vector<int>> sols;

        sort(nums.begin(), nums.end());
        int a = 0; 

        while (a < nums.size()){

            int b = a + 1; 
            int c = nums.size() - 1; 

            while (b < c){
                int x = nums[a] + nums[b] + nums[c];
                if (x < 0) b++; 
                else if (x > 0) c--; 
                else{
                    sols.insert({nums[a], nums[b], nums[c]});
                    b++; 
                    c--; 
                }
            }
            a++; 
        }

        for (auto& x : sols){
            res.emplace_back(x);
        }

        return res;
    }
};