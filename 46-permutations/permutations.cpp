class Solution {
public:

    vector<bool> chosen;
    vector<int> curr = {};
    vector<vector<int>> output = {};

    void search(int i, vector<int>& nums){
        if (i == chosen.size()){
            output.push_back(curr);
            return;
        }

        for (int j = 0; j < chosen.size(); j++){
            if (chosen[j]) continue;
            curr.push_back(nums[j]);
            chosen[j] = true; 
            search(i + 1, nums);
            chosen[j] = false; 
            curr.pop_back(); 
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        
        chosen = vector<bool>(nums.size(), false);
        search(0, nums);
        return output;
    }
};