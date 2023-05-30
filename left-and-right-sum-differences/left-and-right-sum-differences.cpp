// class Solution {
// public:
//     vector<int> leftRightDifference(vector<int>& nums) {
//         vector<int> ans(nums.size());
//         // ans contains all the left sums
//         int left = 0; 
//         for (int i = 0; i < nums.size(); i++){
//             ans[i] = left; 
//             left += nums[i];
//         }

//         // Now we have all the left sums
//         // Now lets do the opposite with the right sums, but subtract the right sums 
//         int right = 0; 
//         for (int i = nums.size() - 1; i >= 0; i--){
//             ans[i] = abs(ans[i] - right); 
//             right += nums[i];
//         }

//         return ans; 
//     }
// };

// Prefix and post
class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        vector<int> ans(nums.size(), 0);

        for (int i = 1; i < nums.size(); i++){
            ans[i] = ans[i - 1] + nums[i - 1];
        }

        int right = 0; 
        for (int i = nums.size() - 1; i >= 0; i--){
            ans[i] = abs(ans[i] - right); 
            right += nums[i];
        }

        return ans; 
    }
};