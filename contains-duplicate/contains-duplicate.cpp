class Solution {
public:
    // bool containsDuplicate(vector<int>& nums) {
    //     // Brute Force O(n^2) 
    //     for (int i = 0; i < nums.size(); i++){
    //         for (int j = i + 1; j < nums.size(); j++){
    //             if (nums[i] == nums[j]) return true;
    //         }
    //     }
        
    //     return false; 
    // }

    bool containsDuplicate(vector<int>& nums) {

        // Sort, then iterate through and check 
        // O(n * Log(n))

        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 1; i++){
            if (nums[i] == nums[i + 1]) return true; 
        }
        
        return false; 
    }
};