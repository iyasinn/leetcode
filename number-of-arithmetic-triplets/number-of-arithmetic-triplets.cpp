class Solution {
public:

    // U: Strictly Increasing Integers
    // M: 
    // We can have a set of all integers
    // And then we can find some O(n) solution that would let us find the perfect j value 
    // 

    int arithmeticTriplets(vector<int>& nums, int diff) {
        int count = 0; 
        for (int i = 0; i < nums.size(); i++){
            for (int j = i + 1; j < nums.size(); j++){
                for (int k = j + 1; k < nums.size(); k++){
                    if (nums[j] - nums[i] == diff && nums[k] - nums[j] == diff){
                        count++; 
                    }
                }
            }
        }
        return count; 
    }
};