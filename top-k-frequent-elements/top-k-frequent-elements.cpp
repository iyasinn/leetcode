class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        unordered_map<int, int> count;
        for (auto val : nums){
            count[val]++;
        }

        auto cmp = [](pair<int, int> a, pair<int, int> b){ return a.second >= b.second; };

        priority_queue<pair<int, int>, 
                       vector<pair<int, int>>, 
                       decltype(cmp)> 
                       pq(cmp); 

        for (auto x : count){
            pq.push({x.first, x.second});
        }

        
        while (pq.size() > k){
            pq.pop();
        }

        vector<int> sol;

        while (!pq.empty()){
            sol.push_back(pq.top().first);
            pq.pop();
        }

    
        return sol;
    }
};