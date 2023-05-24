class Solution {
public:

    
    // // O(n^2 log(n))
    // vector<vector<int>> threeSum(vector<int>& nums) {
    //     // Once we have two pointers, we just need to find the exact third number. 
    //     // Only can work when sorted

    //     sort(nums.begin(), nums.end());

    //     vector<vector<int>> sols;
    //     int start = 0; 

    //     // O(n)
    //     while (start < nums.size()){
    //         // Doe sthis kind of become a 2 sum with the remaining array? 
    //         // We can reduce this problem to a sort of two sum. 
    //         int twoSum = -1 * nums[start];
    //         int low = start + 1; 
    //         int hi = nums.size() - 1; 

    //         // O(n)
    //         while (low < hi){
    //             if (nums[low] + nums[hi] == twoSum){
    //                 sols.push_back({nums[start], nums[low], nums[hi]});
    //                 // To avoid duplicates, we want to skip over the SAME numbers
    //                 // Mathematically, once a low and hi have been used, they are the only unique combo
    //                 // That may work. There may exist other combos, but the low and hi MUST change

    //                 // O(log(n))
    //                 low = upper_bound(nums.begin(), nums.end(), nums[low]) - nums.begin();
    //                 hi = lower_bound(nums.begin(), nums.end(), nums[hi]) - nums.begin();;
    //             }
    //             else if (nums[low] + nums[hi] < twoSum){
    //                 low++;
    //             }
    //             else if (nums[low] + nums[hi] > twoSum){
    //                 hi--; 
    //             }
    //         }

    //         start = (upper_bound(nums.begin(), nums.end(), nums[start]) - nums.begin());
    //         // start++;
    //     }

    //     return sols;
    // }

    

    vector<vector<int>> threeSum(vector<int>& nums) {
        
        // Sorting allows us to take account of tools like binary search!
        sort(nums.begin(), nums.end());
        vector<vector<int>> sols;
        int a = 0; 
        while (a < nums.size()){

            int b = a + 1; 
            int c = nums.size() - 1; 

            while (b < c){

                if (nums[a] + nums[b] + nums[c] == 0){
                    sols.push_back({nums[a], nums[b], nums[c]});
                    b++;
                    c--; 
                    while (b < c && nums[b] == nums[b - 1]){
                        b++;
                    }
                }
                else if (nums[a] + nums[b] + nums[c] < 0){
                    b++; 
                }
                else{
                    c--; 
                } 
            }

            a++; 
            while (a < nums.size() && nums[a] == nums[a - 1]){
                a++; 
            }
        }

        return sols;
    }

    // // O(n^2) but slow because it takes time to fill up that unordered map
    // vector<vector<int>> threeSum(vector<int>& nums) {
        
    //     // Sorting allows us to take account of tools like binary search!
    //     sort(nums.begin(), nums.end());
    //     unordered_map<int, int> mp; 
    //     for (int i = 0; i < nums.size(); i++){
    //         mp[nums[i]] = max(mp[nums[i]], i);
    //     }

    //     vector<vector<int>> sols;

    //     int start = 0; 
    //     int end = 0; 

    //     while (start < nums.size()){

    //         end = start + 1; 
            
    //         while (end < nums.size()){
    //             int find = -1 * (nums[start] + nums[end]);
    //             if (mp[find] > end){
    //                 sols.push_back({nums[start], nums[end], find});
    //             }
    //             end = mp[nums[end]] + 1; 
    //         }
    //         start = mp[nums[start]] + 1; 
    //     }

    //     return sols;
    // }



};































