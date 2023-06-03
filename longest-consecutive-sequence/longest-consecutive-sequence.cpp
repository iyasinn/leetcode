class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        unordered_set<int> mp(nums.begin(), nums.end());
        int best = 0; 
        
        for (int n : nums){
            if (mp.count(n - 1)) continue;

            int curr = 0; 

            while (mp.count(n++)){
                curr++;
            }
            best = max(best, curr);
        
        }
        return best; 
    }


    // int longestConsecutive(vector<int>& nums) {        
    //     sort(nums.begin(), nums.end());
    //     if(nums.size()==0) return 0;
    //     int maxcounter=0, counter=1;
    //     for(int i=1;i<nums.size();i++){
    //         if(nums[i]==nums[i-1]+1){
    //            counter++;
    //         }
    //         else if(nums[i]!=nums[i-1]) {
    //             maxcounter = max(maxcounter, counter);
    //             counter=1;
    //         }
    //     }
    //     maxcounter = max(maxcounter, counter);
    //     return maxcounter;
    // }


    // int longestConsecutive(vector<int>& nums) {

    //     unordered_set<int> numSet(nums.begin(), nums.end());
    //     int maxCount = 0;
        
    //     for (int num : numSet) {
    //         if (!numSet.) {

    //             int count = 1;
                
    //             while (numSet.find(num + 1) != numSet.end()) {
    //                 num++;
    //                 count++;
    //             }
        
    //             maxCount = max(maxCount, count);  
    //         }
    //     }
        
    //     return maxCount;
    // }

};