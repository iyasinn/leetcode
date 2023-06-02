class Solution {
public:
    // int longestConsecutive(vector<int>& nums) {
    
    //     unordered_set<int> mp(nums.begin(), nums.end());
    //     int best = 0; 

    //     for (int& n : nums){
    //         if (mp.count(n - 1)){
    //             continue; 
    //         }
    //         int curr = 0; 
    //         while (mp.count(n)){
    //             n++; 
    //             curr++;
    //         }
    //         best = max(best, curr);
    //     }

    //     return best; 
    // }


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


        int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        
        unordered_set<int> numSet(nums.begin(), nums.end());
        int maxCount = 1;
        
        for (int num : numSet) {
            if (numSet.find(num - 1) == numSet.end()) {  // Check if the current element is the start of a subsequence
                int currNum = num;
                int count = 1;
                
                while (numSet.find(currNum + 1) != numSet.end()) {  // Count consecutive elements
                    currNum++;
                    count++;
                }
                
                maxCount = max(maxCount, count);  // Update the maximum count
            }
        }
        
        return maxCount;
    }

};