class Solution {
public:



    int threeSumClosest(vector<int>& nums, int target) {

        double closest = numeric_limits<double>::infinity(); 
        sort(nums.begin(), nums.end());

        for (int a = 0; a < nums.size(); a++){
            
            int find = target - nums[a];
            int b = a + 1; 
            int c = nums.size() - 1; 

            while (b < c){

                int sum = nums[a] + nums[b] + nums[c];
                if (sum > target){
                    c--; 
                }
                else if (sum < target){
                    b++; 
                }
                else {
                    return sum; 
                }
                closest = (abs(sum - target) < abs(closest - target)) ? sum : closest;
            }
        }

        return closest; 
    }
};