class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        int solution = 0;
        uint curr = 0;
        for (auto n : nums) curr ^= n; 

        for (int i = 0; i < (1 << nums.size()); i++){
            int temp = curr; 
            for (int j = 0; j < nums.size(); j++){
                if ((1 << j) & i) temp ^= nums[j];
            }
            solution += temp; 
        }

        return solution;
    }
};


