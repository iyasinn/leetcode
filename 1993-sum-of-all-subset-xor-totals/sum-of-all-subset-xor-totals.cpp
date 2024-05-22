class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        int solution = 0;

        for (int i = 0; i < (1 << nums.size()); i++){
            uint temp = 0; 
            for (int j = 0; j < nums.size(); j++){
                if ((1 << j) & i) temp ^= nums[j];
            }
            solution += temp; 
        }

        return solution;
    }
};


