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
    int rec(vector<int>& n1, vector<int>& n2, int F, int S, vector<vector<int>>& memo){

        if (F < 0 || F >= n1.size() || S < 0 || S >= n2.size()){
            return 0;
        }
        else if (memo[F][S] != -1){
            return memo[F][S];
        }

        int temp = -1; 

        // Check if there's an element we can draw a line to.
        // Greedily find closest one, then recursively call function
        for (int j = S; j >= 0; j--){
            if (n1[F] == n2[j]){
                temp = rec(n1, n2, F - 1, j - 1, memo) + 1;
                break;
            }
        }

        // Case where we dont draw a line with curr index
        memo[F][S] = max(temp, rec(n1, n2, F - 1, S, memo));
        return memo[F][S];
    }

    int maxUncrossedLines(vector<int>& n1, vector<int>& n2) {
        vector<vector<int>> memo(n1.size(), vector<int>(n2.size(), -1));
        for (auto& row : memo){}
        return rec(n1, n2, n1.size() - 1, n2.size() - 1, memo);
    }



    // bottom up solution


};



