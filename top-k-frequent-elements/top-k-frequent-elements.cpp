class Solution {
public:

    // Time: O(n log k ) 
    // Space: O(n)
    // vector<int> topKFrequent(vector<int>& nums, int k) {
        
    //     // O(n) time, O(n) space
    //     unordered_map<int, int> count;
    //     for (auto val : nums){
    //         count[val]++;
    //     }
        
    //     // pq works with pairs. Compares first value, then second if there's a tie. 
    //     // We are creating a min heap, hence the use of std::greater
    //     priority_queue<pair<int, int>, 
    //                    vector<pair<int, int>>, 
    //                    std::greater<pair<int,int>>>
    //                    pq;
        
    //     // O(n log k) time, O(k) space
    //     // Note we compare first value first, specifically because x.second is the count 
    //     // inside the hashmap. This is the important value, so we use it
    //     for (pair<const int, int>& x : count){
    //         pq.push({x.second, x.first});
    //         if (pq.size() > k){ pq.pop(); }
    //     }

    //     vector<int> sol; 
    //     sol.reserve(k);

    //     // O(k) time, O(k) space
    //     while (!pq.empty()){
    //         sol.emplace_back(pq.top().second);
    //         pq.pop();
    //     }

    //     return sol;
    // }


    vector<int> topKFrequent(vector<int>& nums, int k) {

        unordered_map<int, int> count;
        for (auto val : nums) count[val]++;

        vector<pair<int, int>> vec; 
        for (pair<const int, int>& p : count){ vec.push_back({p.second, p.first}); }

        sort(vec.begin(), vec.end(), greater<pair<int, int>>());
        vector<int> sol(k); 
        transform(vec.begin(), vec.begin() + k, sol.begin(), [](pair<const int, int> p){ return p.second; });

        return sol;

    }

};