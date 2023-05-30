class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans(nums.size() * 2);
        for (int i = 0; i < nums.size(); i++){
            ans[i] = ans[nums.size() + i] = nums[i];
        }
        return ans; 
    }
};
