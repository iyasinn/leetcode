class Solution {
public:

    // U: Strictly Increasing Integers
    // M: 
    // We can have a set of all integers
    // And then we can find some O(n) solution that would let us find the perfect j value 
    // 

    // O(n^3) 
    // int arithmeticTriplets(vector<int>& nums, int diff) {
    //     int count = 0; 
    //     for (int i = 0; i < nums.size(); i++){
    //         for (int j = i + 1; j < nums.size(); j++){
    //             for (int k = j + 1; k < nums.size(); k++){
    //                 if (nums[j] - nums[i] == diff && nums[k] - nums[j] == diff){
    //                     count++; 
    //                 }
    //             }
    //         }
    //     }
    //     return count; 
    // }


    int arithmeticTriplets(vector<int>& nums, int diff) {

        unordered_set<int> s(nums.begin(), nums.end());

        int count = 0; 
        for (int i = 0; i < nums.size(); i++){
            for (int k = i + 2; k < nums.size(); k++){
                int j = nums[i] + diff; 
                if (j == nums[k] - diff && s.count(j)){
                    count++;
                }
            }
        }
        return count; 
    }

};














