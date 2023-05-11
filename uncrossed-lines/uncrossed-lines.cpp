class Solution {
public:
    // int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
    //     // Defining a no-entry range
    //     // If nums2[j] == 0, then it has a line to it
    //     // Greedy algorithm
    //     // Gets first point of difference
    //     int count = 0; 
    //     int start = 0; 

    //     for (int i = 0; i < nums1.size(); i++){
    //         for (int j = start; j < nums2.size(); j++){
    //             if (nums1[i] == nums2[j]){
    //                 count++; 
    //                 start = j + 1; 
    //                 break;
    //             }
    //         }
    //     }
    
    //     return count;
    // }



    // F is the last index of nums 1, S is last index of nums 2  
    int rec(vector<int>& nums1, vector<int>& nums2, int F, int S, vector<vector<int>>& memo){

        if (!(0 <= F && F <= nums1.size()) || !(0 <= S && S <= nums2.size())){
            return 0;
        }

        if (memo[F][S] != -1){
            return memo[F][S];
        }

        int temp = -1; 

        for (int j = S; j >= 0; j--){
            if (nums1[F] == nums2[j]){
                temp = rec(nums1, nums2, F - 1, j - 1, memo) + 1;
                break;
            }
        }

        memo[F][S] = max(temp, rec(nums1, nums2, F - 1, S, memo));
        return memo[F][S];
    }


    int maxUncrossedLines(vector<int>& n1, vector<int>& n2) {
        
        vector<vector<int>> memo(n1.size(), vector<int>(n2.size(), -1));

        return rec(n1, n2, n1.size() - 1, n2.size() - 1, memo);
    }

};



