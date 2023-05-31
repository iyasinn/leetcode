class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        vector<vector<int>> res; 
        sort(nums.begin(), nums.end());
        int a = 0; 

        while (a < nums.size()){

            int b = a + 1; 
            int c = nums.size() - 1; 

            while (b < c){

                if (nums[a] + nums[b] + nums[c] > 0){
                    c--; 
                    continue; 
                }
                else if (nums[a] + nums[b] + nums[c] < 0){
                    b++;
                    continue; 
                }

                res.push_back({nums[a], nums[b], nums[c]}); 
                b++; 
                c--; 
                while (b < c && nums[b] == nums[b - 1]) b++; 
                while (b < c && nums[c] == nums[c + 1]) c--;
            }

            a++; 
            while (a < nums.size() && nums[a] == nums[a - 1]) a++;
        }


        return res;
    }
};