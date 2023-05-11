class Solution {
public:

    // O(n log n) 
    // Sorting solution 
    // vector<int> minSubsequence(vector<int>& nums) {
    //     sort(nums.begin(), nums.end());
    //     int total = 0; 
    //     for (auto n : nums){ total += n; }
    //     vector<int> sol; 
    //     int curr = 0; 
    //     for (int i = nums.size() - 1; i >= 0; i--){
    //         if (curr > total){
    //             break;
    //         }
    //         sol.push_back(nums[i]);
    //         total -= nums[i];
    //         curr += nums[i];
    //     }
    //     return sol; 
    // }


    // auto minSubsequence(vector<int>& nums){

    //     int total = 0; 

    //     for (int n : nums) total += n;

    //     int start = 0; 
    //     int running = 0; 
    //     int bestTotal = 0; 
    //     pair<int, int> index; 
        
    //     for (int end = 0; end < nums.size(); end++){

    //         running += nums[end];
    //         total -= nums[end]; 

    //         while (running - nums[start] >= total + nums[start] && start <= end){
    //             running -= nums[start];
    //             total += nums[start];
    //             start++;
    //         }
    
    //         if (running > bestTotal){
    //             bestTotal = running;
    //             index = make_pair(start, end);
    //         }
    //     }
        
    //     cout << index.first <<  " " << index.second << endl;
        

    //     vector<int> sol; 

    //     for (int i = index.first; i <= index.second; i++){
    //         sol.push_back(nums[i]);
    //     }

    //     sort(sol.begin(), sol.end(), greater<int>());
    //     return sol; 
    // }


    // // We can do a fully greedy solution!
    // vector<int> minSubsequence(vector<int>& nums){

    //     // The largest value is always inlcuded in this sum!
    //     // Then we greedily choose the next largest value to its right or left?

    //     int total = 0; 
    //     int curr = 0; 
    //     vector<int> sol;
    //     sol.reserve(nums.size());

    //     for (auto x : nums) { total += x; }

    //     int left = max_element(nums.begin(), nums.end()) - nums.begin();
    //     int right = left + 1; 

    //     while (curr <= total){
    //         bool lAvailable = 0 <= left && left < nums.size();
    //         bool rAvailable = 0 <= right && right < nums.size();

    //         int temp = 0; 
    //         if (lAvailable) { 
    //             temp = max(temp, nums[left]); 
    //         }
    //         if (rAvailable) { 
    //             temp = max(temp, nums[right]); 
    //         }

    //         if (lAvailable && temp == nums[left]){
    //             left--;
    //         }
    //         else if (rAvailable && temp == nums[right]){
    //             right++;
    //         }

    //         curr += temp;
    //         total -= temp; 
    //         sol.push_back(temp);
    //     }


    //     sort(sol.begin(), sol.end(), greater<int>());
    //     return sol;
    // }


        vector<int> minSubsequence(vector<int>& nums){

        // The largest value is always inlcuded in this sum!
        // Then we greedily choose the next largest value to its right or left?

        // We can employ a bucket srot

        int total = 0; 

        vector<int> freq(101);

        for (auto x : nums){
            total += x; 
            freq[x]++;
        }

        int curr = 0;
        vector<int> sol;
        sol.reserve(nums.size());

        for (int i = 100; i >= 1; i--){
            while (curr <= total && freq[i] > 0){
                total -= i; 
                curr += i; 
                sol.push_back(i);
                freq[i]--;
            }
        }

        return sol; 






















    }

};