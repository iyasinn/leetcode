class Solution {
public:
    // int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        
    //     int count = 0; 

    //     for (int start = 0; start < nums.size(); start++){
            
    //         // Exclusive range: [start, end)
    //         int product = nums[start];
    //         int end = start + 1; 

    //         while (end < nums.size() && product < k){
    //             count++; 
    //             product *= nums[end];
    //             end++;
    //         }

    //         if (end == nums.size() && product < k){ count++; }
    //     }

    //     return count; 
        
    // }

    // Optimize our sliding window!
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        
        int count = 0; 
        int end = 0; 
        int product = 1;

        for (int start = 0; start < nums.size(); start++){

            if (start > end){ 
                end = start;
                product = 1;
            }

            // Checks if adding next available value keeps our product small
            while (end < nums.size() && (nums[end] * product) < k){
                product *= nums[end];
                end++;
            }

            count += (end - start); 
            product /= nums[start];
        }

        return count; 
        
    }

};