class Solution {
public:

    // O(n^2)
    // int longestConsecutive(vector<int>& nums) {
    //     // We would probably need to do multiple runs
    //     // As we iterate over each element, what info do we get? 
    //     // We get its start point
    //     // Everything that is one diff away has the same start point
    //     // We want O(1) lookup, to determine if specific integers exist, so maybe we could look into a set 

    //     unordered_set<int> n(nums.begin(), nums.end());
    //     int best = 0; 

    //     for (int i = 0; i < nums.size(); i++){

    //         int count = 1; 
    //         int curr = nums[i];

    //         while (n.count(++curr)){
    //             count++;
    //         }

    //         best = max(best, count);
    //     }

    //     return best; 
    // }


    //THINK ABOUT PROPERTIES
    // THINK ABOUT SEQUNcCES OF NUMBERS 
    // AND WHAT PROPERTIES THEY MAY HAVE 

    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0; 
        unordered_set<int> n(nums.begin(), nums.end());
        int best = 1; 

        for (int i = 0; i < nums.size(); i++){

            int count = 1; 
            int curr = nums[i];

            if (n.count(curr - 1) || !n.count(curr + 1)){
                continue; 
            }

            while (n.count(curr + 1)){
                count++;
                curr++;
            }

            best = max(best, count);
        }

        return best; 
    }
};