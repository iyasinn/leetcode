class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {


        int best = 0;
        int freq = 0; 

        for (int subset = 0; subset < pow(2, nums.size()); subset += 1){

            int curr = 0; 

            for (int i = 0; i < nums.size(); i++){
                if ((subset >> i) & 1){
                    curr = curr | nums[i];
                }
            }

            if (curr == best){
                freq += 1; 
            }
            else if (curr > best){
                freq = 1; 
                best = curr; 
            }

        }

        return freq; 
    }
};