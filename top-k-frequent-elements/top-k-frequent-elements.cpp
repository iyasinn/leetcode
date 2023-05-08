class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        unordered_map<int, int> count;
        for (auto val : nums){
            count[val]++;
        }
        priority_queue<pair<int, int>, 
                       vector<pair<int, int>>, 
                       std::greater<pair<int,int>>>
                       pq;
        
        for (pair<const int, int>& x : count){
            pq.push({x.second, x.first});
            if (pq.size() > k){ pq.pop(); }
        }

        vector<int> sol; 
        sol.reserve(k);

        while (!pq.empty()){
            sol.emplace_back(pq.top().second);
            pq.pop();
        }

        return sol;
    }
};