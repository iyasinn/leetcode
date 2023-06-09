

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

    // bool containsDuplicate(vector<int>& nums) {

    //     // Sort, then iterate through and check 
    //     // O(n * Log(n))

    //     sort(nums.begin(), nums.end());

    //     for (int i = 0; i < nums.size() - 1; i++){
    //         if (nums[i] == nums[i + 1]) return true; 
    //     }
        
    //     return false; 
    // }


    // bool containsDuplicate(vector<int>& nums) {

    //     // Set
    //     // O(n) insertion, and O(1) retrievl
    //     int x; 

    //     unordered_set<int> val;

    //     for (int i = 0; i < nums.size(); i++){
    //         if (val.insert(nums[i]).second == false){
    //             return true; 
    //         }
    //     }
        
    //     return false; 
    // }

    bool containsDuplicate(vector<int>& nums){
        return unordered_set<int>(nums.begin(), nums.end()).size() != nums.size();
    }

    // bool containsDuplicate(vector<int>& nums){
    //     unordered_set<int> m(nums.begin(), nums.end());
    //     return m.size() != nums.size();
    // }


};