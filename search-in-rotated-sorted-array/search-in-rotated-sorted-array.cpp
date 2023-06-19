class Solution {
public:

    int search(vector<int>& nums, int target) {
        // Can we reduce this to the the find minimum problem? 
        int start = 0; 
        int end = nums.size() - 1;

        // for (auto x : nums){
        //     cout << x << " ";
        // }
        // cout << endl;
        // for (int i = 0; i < nums.size(); i++){
        //     cout << i << " ";
        // }
        // cout << endl << endl;


        // To see if in left or right portion is very easy 
        // If larger than end, the nyou are in left portion, if smaller than end, then you are in large portion

        while (start <= end){
            int mid = start + (end - start) / 2; 

            // cout << mid << endl;
            if (nums[mid] == target) return mid; 

            // In left section
            if (nums[mid] > nums[end]){
                if (target < nums[mid] && nums[start] <= target){
                    end = mid - 1; 
                }
                else { start = mid + 1; }
            }
            // If in right portion 
            else {
                if (target > nums[mid] && target <= nums[end]){
                    start = mid + 1; 
                }
                else {end = mid - 1; }
            }
        }
        return -1; 
    }
};