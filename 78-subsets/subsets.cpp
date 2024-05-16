class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        
        // i < 2^(n)
        vector<vector<int>> output; 

        for (int binval = 0; binval < (1 << nums.size()); binval++){
            vector<int> subset; 
            for (int index = 0; index < nums.size(); index++){
                if ((1 << index) & binval){
                    subset.push_back(nums[index]);
                } 
            }

            output.push_back(subset);
        }
        return output;
    }
};