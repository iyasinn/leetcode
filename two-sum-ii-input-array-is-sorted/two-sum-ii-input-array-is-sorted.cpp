class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        int start = 0; 
        int end = nums.size() - 1; 

        while (start < end){
            int temp = nums[start] + nums[end];
            if (temp == target){ return {start + 1, end + 1}; }

            start += (temp < target);
            end -= (temp > target);
        }

        return {};
    }
};