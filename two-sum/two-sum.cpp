class Solution {
public:
    
    // O(n^2) solution
    // vector<int> twoSum(vector<int>& nums, int target) {
    //     for (int i = 0; i < nums.size(); i++){
    //         for (int j = i + 1; j < nums.size(); j++){
    //             if (nums[i] + nums[j] == target){
    //                 return {i, j};
    //             }
    //         }
    //     }
    //     return {};
    // }

    // O(n) time, O(n) space
    // The big idea here is that we are looking for the target numbers index essentially
    // Hashmap is storing (number, index) and if target - curr is number, then we got both idnexes
    vector<int> twoSum(vector<int>& nums, int target) {
        
        // Value and its index
        unordered_map<int, int> output; 

        for (int i = 0; i < nums.size(); i++){
             if (output.count(target - nums[i])){
                    return {output[target - nums[i]], i};
                }  
            output[nums[i]] = i; 
        }
        return {};
    }
};