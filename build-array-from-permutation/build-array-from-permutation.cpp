class Solution {
public:
    inline vector<int> buildArray(vector<int>& nums) {
        std::ios_base::sync_with_stdio(false);
        if(nums.size() == 0){return {}; }
        vector<int> ans(nums.size()); 
        for (int i = 0; i < ans.size(); i++){
            ans[i] = nums[nums[i]];
        }
        return ans;
    }
};