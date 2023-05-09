class Solution {
public:

    // O(n^2) solution
    // O(1) space
    // vector<int> productExceptSelf(vector<int>& nums) {

    //     vector<int> sol; 

    //     for (int i = 0; i < nums.size(); i++){

    //         int prod = 1; 

    //         for (int j = 0; j < nums.size(); j++){
    //             if (j == i) continue; 
    //             prod *= nums[j];
    //         }
    //         sol.push_back(prod); 
    //     }

    //     return sol; 
    // }


    vector<int> productExceptSelf(vector<int>& nums) {

        vector<int> ans(nums.size(), 1);

        // Stores all values to the left of nums[i]
        // We get this by taking the value to the left of nums[i], and multiple it by 
        // All the vlaues multipled to the left of it, which is stored in ans
        for (int i = 1; i < nums.size(); i++){
            ans[i] = nums[i - 1] * ans[i - 1];
        }

        int right = 1; 

        for (int i = nums.size() - 1; i >= 0; i--){
            ans[i] = ans[i] * right; 
            right *= nums[i];
        }

        return ans; 
    }


};







