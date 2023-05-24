class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // Once we have two pointers, we just need to find the exact third number. 
        // Only can work when sorted

        sort(nums.begin(), nums.end());

        vector<vector<int>> sols;
        int start = 0; 

        while (start < nums.size()){
            // Doe sthis kind of become a 2 sum with the remaining array? 
            // We can reduce this problem to a sort of two sum. 
            int twoSum = -1 * nums[start];
            int low = start + 1; 
            int hi = nums.size() - 1; 

            while (low < hi){
                if (nums[low] + nums[hi] == twoSum){
                    sols.push_back({nums[start], nums[low], nums[hi]});
                    low = upper_bound(nums.begin(), nums.end(), nums[low]) - nums.begin();
                    hi = lower_bound(nums.begin(), nums.end(), nums[hi]) - nums.begin();;
                }
                else if (nums[low] + nums[hi] < twoSum){
                    low++;
                }
                else if (nums[low] + nums[hi] > twoSum){
                    hi--; 
                }
            }

            start = (upper_bound(nums.begin(), nums.end(), nums[start]) - nums.begin());
            // start++;
        }

   
        return sols;
    }
};