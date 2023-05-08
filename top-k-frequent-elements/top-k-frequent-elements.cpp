class Solution {
public:

    // // Time: O(n log k ) 
    // // Space: O(n)
    // vector<int> topKFrequent(vector<int>& nums, int k) {

    //     unordered_map<int, int> count;
    //     for (auto val : nums){
    //         count[val]++;
    //     }

    //     priority_queue<pair<int, int>, 
    //                    vector<pair<int, int>>, 
    //                    std::greater<pair<int,int>>>
    //                    pq;
        

    //     for (pair<const int, int>& x : count){
    //         pq.push({x.second, x.first});
    //         if (pq.size() > k){ pq.pop(); }
    //     }

    //     vector<int> sol; 
    //     sol.reserve(k);


    //     while (!pq.empty()){
    //         sol.emplace_back(pq.top().second);
    //         pq.pop();
    //     }

    //     return sol;
    // }


    // Array method
    // O(n log n) complexity, does not pass the requirements
    // vector<int> topKFrequent(vector<int>& nums, int k) {

    //     unordered_map<int, int> count;
    //     for (auto val : nums) count[val]++;

    //     vector<pair<int, int>> vec; 
    //     for (pair<const int, int>& p : count){ vec.push_back({p.second, p.first}); }

    //     sort(vec.begin(), vec.end(), greater<pair<int, int>>());
    //     vector<int> sol(k); 
    //     transform(vec.begin(), vec.begin() + k, sol.begin(), [](pair<const int, int> p){ return p.second; });

    //     return sol;
    // }

    // vector<int> topKFrequent(vector<int>& nums, int k) {

    //     unordered_map<int, int> count;
    //     vector<int> solution;
    //     for (auto val : nums) count[val]++;
    //     vector<pair<int, int>> vec; 
    //     for (pair<const int, int>& p : count){ vec.push_back({p.second, p.first}); }
    //     std::nth_element(vec.begin(), vec.begin() + k, vec.end(), std::greater<pair<int,int>>());
    //     for (int i = 0; i < k; i++){ solution.emplace_back(vec[i].second);}
    //     return solution;
    // }

    // O(n) solution
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<int> solution;
        for (auto& val : nums) count[val]++;
        vector<pair<int, int>> vec; 
        for (auto& p : count){ vec.push_back({p.second, p.first}); }
        std::nth_element(vec.begin(), vec.end() - k, vec.end());
        for (int i = vec.size() - k; i < vec.size(); i++){ solution.emplace_back(vec[i].second);}
        return solution;
    }

};











